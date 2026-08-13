import bpy
from .panels import EXPORTER_PT_sidebar, EXPORTER_PT_main_settings, SUFFIXER_PT_main_settings, EXPORTER_PT_Temp

CLASSES = [
    EXPORTER_PT_sidebar,
    EXPORTER_PT_main_settings,
    EXPORTER_PT_Temp,
    SUFFIXER_PT_main_settings,
]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)




def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)