import bpy

from bpy.props import (
    CollectionProperty,
    IntProperty,
    StringProperty,
)

from .properties import (
    ExporterAssetTypeProperties,
    ExporterRuleItem,
    )

from .operators import (
    EXPORTER_OT_asset_type_add,
    EXPORTER_OT_asset_type_remove,
    EXPORTER_OT_load_config,
    EXPORTER_OT_save_config,
    EXPORTER_OT_rule_add,
    EXPORTER_OT_rule_remove
)

from .ui import (
    EXPORTER_UL_asset_types,
    EXPORTER_UL_rules,
    EXPORTER_PT_asset_types,
)


CLASSES = (
    ExporterRuleItem,
    ExporterAssetTypeProperties,

    EXPORTER_OT_asset_type_add,
    EXPORTER_OT_asset_type_remove,

    EXPORTER_OT_save_config,
    EXPORTER_OT_load_config,

    EXPORTER_OT_rule_add,
    EXPORTER_OT_rule_remove,

    EXPORTER_UL_asset_types,
    EXPORTER_UL_rules,
    EXPORTER_PT_asset_types,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

    bpy.types.Scene.exporter_asset_types = CollectionProperty(
        type=ExporterAssetTypeProperties,
    )

    bpy.types.Scene.exporter_asset_type_index = IntProperty(
        default=0,
    )

    bpy.types.Scene.exporter_project_dir = StringProperty(
        name="Project Directory",
        subtype="DIR_PATH",
    )

def unregister():
    del bpy.types.Scene.exporter_asset_type_index
    del bpy.types.Scene.exporter_asset_types
    del bpy.types.Scene.exporter_project_dir


    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)