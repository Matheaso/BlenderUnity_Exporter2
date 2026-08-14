from bpy.props import EnumProperty
from bpy.types import PropertyGroup

from adapters.blender_adapter.helpers import get_blender_asset_types


class ExportSettings(PropertyGroup):
    asset_type: EnumProperty(
        name="Asset Type",
        items=get_blender_asset_types,
        default=0
    )



