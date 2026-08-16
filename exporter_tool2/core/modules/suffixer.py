from dataclasses import dataclass

from ..result import Result, Severity
from ..serialization import load_config
from ...core.asset_data import AssetPackage, AssetData


@dataclass(frozen=True)
class RenameOperation:
    old_name: str
    new_name: str


class Suffixer:

    @staticmethod
    def run_suffix(asset_package: AssetPackage, suffix: str) -> Result[list[RenameOperation]]:

        rename_operations: list[RenameOperation] = []

        if asset_package:
            return Result(
                False,
                Severity.WARNING,
                "No objects selected",
            )

        if not suffix:
            return Result(
                False,
                Severity.INFO,
                "No suffix selected"
            )

        suffix = suffix.replace("_", "")

        for obj in asset_package.objects:
            old_name = obj.name

            new_name = obj.name
            if not new_name.endswith("_"):
                new_name += "_"
            new_name += suffix

            rename_operations.append(RenameOperation(old_name, new_name))

        return Result(
            True,
            Severity.INFO,
            "",
            rename_operations
        )

    @staticmethod
    def run_prefix(asset_package: AssetPackage, prefix: str) -> Result[list[RenameOperation]]:

        rename_operations: list[RenameOperation] = []

        if asset_package:
            return Result(
                False,
                Severity.WARNING,
                "No objects selected",
            )

        if not prefix:
            return Result(
                False,
                Severity.INFO,
                "No suffix selected"
            )

        prefix = prefix.replace("_", "")

        for obj in asset_package.objects:
            old_name = obj.name

            new_name = obj.name
            if not new_name.startswith("_"):
                new_name = "_" + new_name
            new_name = f"{prefix}{new_name}"

            rename_operations.append(RenameOperation(old_name, new_name))

        return Result(
            True,
            Severity.INFO,
            "",
            rename_operations
        )

    @staticmethod
    def run_replace(asset_package: AssetPackage, old: str, new: str) -> Result[list[RenameOperation]]:

        rename_operations: list[RenameOperation] = []

        if asset_package:
            return Result(
                False,
                Severity.WARNING,
                "No objects selected",
            )

        if not old:
            return Result(
                False,
                Severity.INFO,
                "No suffix selected"
            )

        for obj in asset_package.objects:
            old_name = obj.name
            new_name = obj.name.replace(old, new)

            rename_operations.append(RenameOperation(old_name, new_name))

        return Result(
            True,
            Severity.INFO,
            "",
            rename_operations
        )

    @staticmethod
    def run_auto(asset_package: AssetPackage, asset_type: str) -> Result[list[RenameOperation]]:

        rename_operations: list[RenameOperation] = []

        if not asset_package.objects:
            return Result(
                False,
                Severity.WARNING,
                "No objects selected",
            )

        if asset_type == "NO_SELECTION":
            return Result(
                False,
                Severity.WARNING,
                "Asset Type not selected",
            )

        config = load_config()

        for t in config.asset_types:
            if t.name_id == asset_type:
                name_convention = t.naming_convention

                for obj in asset_package.objects:
                    old_name = obj.name
                    new_name = name_convention.prefix + old_name + name_convention.suffix
                    rename_operations.append(RenameOperation(old_name, new_name))
                break

        else:
            return Result(
                False,
                Severity.ERROR,
                f"Asset type '{asset_type}' not found",
            )

        return Result(
            True,
            Severity.INFO,
            "",
            rename_operations
        )
