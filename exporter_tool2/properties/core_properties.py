import bpy
from bpy.props import EnumProperty, PointerProperty
from bpy.types import PropertyGroup

from ..core.serialization import load_config

def get_asset_types(self, context):
    return (
        ("NOT_SELECTED", "Not Selected", "Select asset type"),
    ) + load_config().to_tuple_str

class ExportSettings(PropertyGroup):
    asset_type: EnumProperty(
        name="Asset Type",
        items=get_asset_types,
        default=0
    )