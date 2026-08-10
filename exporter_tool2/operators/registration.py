import bpy
from .validate_operator import EXPORT_TOOL_validate

CLASSES = (
    EXPORT_TOOL_validate,

)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    pass