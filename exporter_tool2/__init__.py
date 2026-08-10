import bpy
from .operators import registration as operator_registration
from .ui import registration as ui_registration
from .properties import registration as properties_registration
from .tools import suffixer as suffixer

bl_info = {
    "name": "custom_exporter v2",
    "author": "Maciej Matheas Sojka",
    "version": (0, 1, 0),
    "blender": (4, 1, 0),
    "location": "",
    "description": "",
    "warning": "",
    "category": "Exporter",
}


def register():
    operator_registration.register()
    ui_registration.register()
    properties_registration.register()
    suffixer.register()


    return None


def unregister():
    operator_registration.unregister()
    return None


if __name__ == "__main__":
    register()