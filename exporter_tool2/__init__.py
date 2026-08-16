from .adapters.blender.operators import (
    register as operator_registration,
    unregister as operator_unregister
)
from .adapters.blender.ui import (
    register as ui_register,
    unregister as ui_unregister
)
from .adapters.blender.properties import (
    register as properties_register,
    unregister as properties_unregister
)
from .adapters.blender.modules.bl_suffixer import (
    register as suffixer_register,
    unregister as suffixer_unregister
)

from .adapters.blender.modules.config_tool import (
    register as config_tools_register,
    unregister as config_tools_unregister
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
    properties_register()
    operator_registration()
    ui_register()
    suffixer_register()
    config_tools_register()


    return None


def unregister():
    properties_unregister()
    operator_unregister()
    ui_unregister()
    suffixer_unregister()
    config_tools_unregister()
    return None


if __name__ == "__main__":
    register()