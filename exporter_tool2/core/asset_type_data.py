from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AssetTypeData:
    name_id: str
    display_name: str

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
            }
            for asset in config.asset_types
        ],
    }