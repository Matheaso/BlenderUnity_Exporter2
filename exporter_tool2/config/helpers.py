from ..core.serialization import load_config


def get_asset_types():
    return (
        ("NOT_SELECTED", "Not Selected", "Select asset type"),
    ) + load_config().to_tuple_str