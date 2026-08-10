import json
from pathlib import Path

from .asset_type_data import ExporterConfigData, config_to_dict, AssetTypeData, NamingConvention

ROOT_DIR = Path(__file__).parent.parent
CONFIG_PATH = ROOT_DIR / "config" / "exporter_settings.json"


def save_config(config: ExporterConfigData) -> None:
    data = config_to_dict(config)

    with CONFIG_PATH.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def save_config_as(config: ExporterConfigData, filepath: Path) -> None:
    data = config_to_dict(config)

    with filepath.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_config() -> ExporterConfigData:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    asset_types = tuple(
        AssetTypeData(
            name_id=asset["name_id"],
            display_name=asset["display_name"],
            naming_convention=NamingConvention(
                prefix=asset["naming_convention"]["prefix"],
                suffix=asset["naming_convention"]["suffix"],
            ),
            rule_id=tuple(asset["rule_id"]),
        )
        for asset in data["asset_types"]
    )

    return ExporterConfigData(
        project_dir=ROOT_DIR,
        asset_types=asset_types,
    )
