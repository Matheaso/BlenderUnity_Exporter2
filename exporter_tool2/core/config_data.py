from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class NamingConvention:
    prefix: str
    suffix: str


@dataclass(frozen=True)
class AssetTypeData:
    name_id: str
    display_name: str

    naming_convention: NamingConvention
    rule_id: tuple[str, ...]


@dataclass(frozen=True)
class ExporterConfigData:
    project_dir: Path
    asset_types: tuple[AssetTypeData, ...]

    @property
    def to_tuple_str(self) -> tuple[tuple[str, str, str], ...]:
        return tuple(
            (asset_type.name_id, asset_type.display_name, "")
            for asset_type in self.asset_types
        )


def config_to_dict(config: ExporterConfigData) -> dict:
    return {
        "project_dir": str(config.project_dir),
        "asset_types": [
            {
                "name_id": asset.name_id,
                "display_name": asset.display_name,
                "naming_convention": {
                    "prefix": asset.naming_convention.prefix,
                    "suffix": asset.naming_convention.suffix,
                },
                "rule_id": asset.rule_id,
            }
            for asset in config.asset_types
        ],
    }