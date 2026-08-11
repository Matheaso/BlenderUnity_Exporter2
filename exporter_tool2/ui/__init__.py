import bpy
from .panels import EXPORTERTOOL_PT_sidebar, EXPORTERTOOL_PT_main_settings, SUFFIXER_PT_main_settings

CLASSES = (
    EXPORTERTOOL_PT_sidebar,
    EXPORTERTOOL_PT_main_settings,
    SUFFIXER_PT_main_settings
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)