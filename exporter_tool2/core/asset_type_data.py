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