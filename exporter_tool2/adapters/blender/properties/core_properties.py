from bpy.props import EnumProperty
from bpy.types import PropertyGroup

from exporter_tool2.adapters.blender.helpers import get_blender_asset_types


class ExportSettings(PropertyGroup):
    asset_type: EnumProperty(
        name="Asset Type",
        items=get_blender_asset_types,
        default=0
    )



