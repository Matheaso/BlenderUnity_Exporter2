import bpy
from .validate_operator import EXPORT_TOOL_validate, EXPORT_TOOL_test

CLASSES = (
    EXPORT_TOOL_validate,
    EXPORT_TOOL_test

)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    pass