import bpy

from .collision_shape_operators import (
    EXPORTER_OT_create_collision_shape
)
from .create_export_package import EXPORTER_OT_CreateExportPackage
from .export_operator import  EXPORTER_OT_exporter
from .ui_operators import EXPORTER_OT_collision_module_switch, EXPORTER_OT_lod_module_switch

CLASSES = (
    EXPORTER_OT_exporter,
    EXPORTER_OT_CreateExportPackage,
    EXPORTER_OT_create_collision_shape,
    EXPORTER_OT_collision_module_switch,
    EXPORTER_OT_lod_module_switch,
)

def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)