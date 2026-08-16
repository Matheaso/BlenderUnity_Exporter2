import bpy
from .core_panels import (
    EXPORTER_PT_sidebar,
    EXPORTER_PT_main_settings,
    SUFFIXER_PT_main_settings,
    EXPORTER_PT_Temp,

)

from .module_panels import (
    EXPORTER_PT_lod_module,
    EXPORTER_PT_collision_module
)

CLASSES = [
    #core
    EXPORTER_PT_sidebar,
    EXPORTER_PT_main_settings,
    EXPORTER_PT_Temp,
    SUFFIXER_PT_main_settings,

    #modular
    EXPORTER_PT_lod_module,
    EXPORTER_PT_collision_module,
]


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)