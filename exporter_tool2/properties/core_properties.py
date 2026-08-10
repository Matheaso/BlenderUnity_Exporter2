import bpy
from bpy.props import EnumProperty, PointerProperty
from bpy.types import PropertyGroup

def get_asset_types():
    return []

class ExportSettings(PropertyGroup):
    asset_type: EnumProperty(
        name="Asset Type",
        items=[
            ("MESH", "Mesh", ""),
            ("COLLISION", "Collision", ""),
            ("SOCKET", "Socket", ""),
        ],
        default="MESH",
    )