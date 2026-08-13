import bpy
from bpy.props import EnumProperty

from .properties import rule_enum_items

#TODO: Need to do smth with this imports
from .....core.serialization import (
    ROOT_DIR,
    save_config,
    load_config
)

#TODO: Need to do smth with this imports
from .....core.config_data import (
    AssetTypeData,
    NamingConvention,
    ExporterConfigData)

class EXPORTER_OT_asset_type_add(bpy.types.Operator):
    bl_idname = "exporter.asset_type_add"
    bl_label = "Add Asset Type"
    bl_description = "Add new asset type"

    def execute(self, context):
        scene = context.scene

        item = scene.exporter_asset_types.add()

        item.name_id = "new_asset"
        item.display_name = "New Asset Type"

        scene.exporter_asset_type_index = (
            len(scene.exporter_asset_types) - 1
        )

        return {"FINISHED"}

class EXPORTER_OT_asset_type_remove(bpy.types.Operator):
    bl_idname = "exporter.asset_type_remove"
    bl_label = "Remove Asset Type"
    bl_description = "Remove selected asset type"

    @classmethod
    def poll(cls, context):
        return bool(context.scene.exporter_asset_types)

    def execute(self, context):
        scene = context.scene

        index = scene.exporter_asset_type_index

        scene.exporter_asset_types.remove(index)

        scene.exporter_asset_type_index = min(
            index,
            len(scene.exporter_asset_types) - 1,
        )

        return {"FINISHED"}

class EXPORTER_OT_load_config(bpy.types.Operator):
    bl_idname = "exporter.load_config"
    bl_label = "Load Config"
    bl_description = "Load exporter configuration"

    def execute(self, context):
        try:
            config = load_config()

            config_to_scene(
                context.scene,
                config,
            )

        except Exception as exc:
            self.report(
                {"ERROR"},
                f"Failed to load config: {exc}",
            )
            return {"CANCELLED"}

        self.report(
            {"INFO"},
            "Exporter config loaded",
        )

        return {"FINISHED"}


class EXPORTER_OT_save_config(bpy.types.Operator):
    bl_idname = "exporter.save_config"
    bl_label = "Save Config"
    bl_description = "Save exporter configuration"

    def execute(self, context):
        try:
            config = scene_to_config(context.scene)

            save_config(config)

        except Exception as exc:
            self.report(
                {"ERROR"},
                f"Failed to save config: {exc}",
            )
            return {"CANCELLED"}

        self.report(
            {"INFO"},
            "Exporter config saved",
        )

        return {"FINISHED"}

class EXPORTER_OT_rule_add(bpy.types.Operator):
    bl_idname = "exporter.rule_add"
    bl_label = "Add Rule"

    rule_id: EnumProperty(
        name="Rule",
        items=rule_enum_items,
    )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(
            self,
        )

    def execute(self, context):
        scene = context.scene

        if not scene.exporter_asset_types:
            return {"CANCELLED"}

        asset = scene.exporter_asset_types[
            scene.exporter_asset_type_index
        ]

        existing = {
            item.rule_id
            for item in asset.rules
        }

        if self.rule_id in existing:
            self.report(
                {"WARNING"},
                "Rule already added",
            )
            return {"CANCELLED"}

        item = asset.rules.add()
        item.rule_id = self.rule_id

        asset.rule_index = len(asset.rules) - 1

        for window in context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == "PROPERTIES":
                    area.tag_redraw()

        return {"FINISHED"}


class EXPORTER_OT_rule_remove(bpy.types.Operator):
    bl_idname = "exporter.rule_remove"
    bl_label = "Remove Rule"

    @classmethod
    def poll(cls, context):
        scene = context.scene

        if not scene.exporter_asset_types:
            return False

        index = scene.exporter_asset_type_index

        if not (
            0 <= index < len(scene.exporter_asset_types)
        ):
            return False

        asset = scene.exporter_asset_types[index]

        return bool(asset.rules)

    def execute(self, context):
        scene = context.scene

        asset = scene.exporter_asset_types[
            scene.exporter_asset_type_index
        ]

        index = asset.rule_index

        if 0 <= index < len(asset.rules):
            asset.rules.remove(index)

            asset.rule_index = max(
                0,
                min(
                    index,
                    len(asset.rules) - 1,
                ),
            )

        return {"FINISHED"}

def scene_to_config(scene) -> ExporterConfigData:
    return ExporterConfigData(
        project_dir=scene.exporter_project_dir,

        asset_types=tuple(
            AssetTypeData(
                name_id=item.name_id,
                display_name=item.display_name,
                naming_convention=NamingConvention(
                    prefix=item.naming_prefix,
                    suffix=item.naming_suffix,
                ),
                rule_id=tuple(
                    rule.rule_id
                    for rule in item.rules
                ),
                relative_path=item.relative_path,
            )
            for item in scene.exporter_asset_types
        ),
    )

def config_to_scene(scene, config: ExporterConfigData) -> None:
    scene.exporter_asset_types.clear()

    scene.exporter_project_dir = str(config.project_dir)

    for asset_data in config.asset_types:
        item = scene.exporter_asset_types.add()

        item.name_id = asset_data.name_id
        item.display_name = asset_data.display_name

        item.naming_prefix = asset_data.naming_convention.prefix
        item.naming_suffix = asset_data.naming_convention.suffix
        item.relative_path = asset_data.relative_path

        item.rules.clear()

        for rule_id in asset_data.rule_id:
            rule = item.rules.add()
            rule.rule_id = rule_id

        item.rule_index = 0

    scene.exporter_asset_type_index = 0