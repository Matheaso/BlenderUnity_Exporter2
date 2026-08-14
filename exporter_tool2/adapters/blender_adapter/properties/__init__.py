import bpy
from bpy.props import PointerProperty, IntProperty, BoolProperty

from .core_properties import ExportSettings

classes = (
    ExportSettings,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.export_settings = PointerProperty(type=ExportSettings)

    bpy.types.Scene.lod_number = IntProperty(default=3, min=0, soft_max=7)

    bpy.types.Scene.is_lod = BoolProperty(default=False)

    bpy.types.Scene.is_collision = BoolProperty(default=False)


def unregister():
    del bpy.types.Scene.export_settings
    del bpy.types.Scene.lod_number
    del bpy.types.Scene.is_lod

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)