import bpy
from bpy.props import EnumProperty, PointerProperty
from bpy.types import PropertyGroup

from .helper import get_blender_asset_types

class ExportSettings(PropertyGroup):
    asset_type: EnumProperty(
        name="Asset Type",
        items=get_blender_asset_types,
        default=0
    )



