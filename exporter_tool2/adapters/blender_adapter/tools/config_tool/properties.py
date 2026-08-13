import bpy

from bpy.props import (
    StringProperty,
    CollectionProperty,
    IntProperty,
    EnumProperty,
)

from .....validation.rule_registry import RULE_REGISTRY


def rule_enum_items(self, context):
    return [
        (
            rule_id,
            rule_class.display_name,
            rule_class.description,
        )
        for rule_id, rule_class in RULE_REGISTRY.items()
    ]


class ExporterRuleItem(bpy.types.PropertyGroup):
    rule_id: StringProperty(
        name="Rule ID",
    )

class ExporterAssetTypeProperties(bpy.types.PropertyGroup):
    name_id: StringProperty(
        name="ID",
    )

    display_name: StringProperty(
        name="Display Name",
    )

    naming_prefix: StringProperty(
        name="Prefix",
    )

    naming_suffix: StringProperty(
        name="Suffix",
    )

    rules: CollectionProperty(
        type=ExporterRuleItem,
    )

    rule_index: IntProperty(
        default=0,
    )

    relative_path: bpy.props.StringProperty(
        name="Relative Path",
        default="Assets/Graphics/Import",
    )




