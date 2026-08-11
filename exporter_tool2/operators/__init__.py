import bpy
from .export_operator import  EXPORT_TOOL_exporter

CLASSES = (
    EXPORT_TOOL_exporter,
)

def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    pass