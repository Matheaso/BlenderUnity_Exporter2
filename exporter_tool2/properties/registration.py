import bpy
from bpy.props import PointerProperty

from . core_properties import ExportSettings

classes = (
    ExportSettings,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.export_settings = PointerProperty(
        type=ExportSettings
    )


def unregister():
    del bpy.types.Scene.export_settings

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)