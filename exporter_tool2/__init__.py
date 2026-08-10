from .operators import (
    register as operator_registration,
    unregister as operator_unregister
)
from .ui import (
    register as ui_register,
    unregister as ui_unregister
)
from .properties import (
    register as properties_register,
    unregister as properties_unregister
)
from .tools.suffixer import (
    register as suffixer_register,
    unregister as suffixer_unregister
)

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
    operator_registration()
    ui_register()
    properties_register()
    suffixer_register()


    return None


def unregister():
    return None


if __name__ == "__main__":
    register()