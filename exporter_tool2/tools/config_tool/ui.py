import bpy
from ...validation.rule_registry import RULE_REGISTRY

class EXPORTER_UL_asset_types(bpy.types.UIList):

    def draw_item(
        self,
        context,
        layout,
        data,
        item,
        icon,
        active_data,
        active_propname,
        index,
    ):
        if self.layout_type in {"DEFAULT", "COMPACT"}:
            layout.label(
                text=item.display_name or item.name_id or "New Asset Type",
                icon="ASSET_MANAGER",
            )

        elif self.layout_type == "GRID":
            layout.alignment = "CENTER"
            layout.label(
                text="",
                icon="ASSET_MANAGER",
            )

class EXPORTER_UL_rules(bpy.types.UIList):

    def draw_item(
        self,
        context,
        layout,
        data,
        item,
        icon,
        active_data,
        active_propname,
        index,
    ):
        rule_class = RULE_REGISTRY.get(item.rule_id)

        if rule_class:
            layout.label(
                text=rule_class.display_name,
                icon="CHECKMARK",
            )
        else:
            layout.label(
                text=item.rule_id,
                icon="ERROR",
            )

class EXPORTER_PT_asset_types(bpy.types.Panel):
    bl_label = "Exporter Settings"
    bl_idname = "EXPORTER_PT_asset_types"

    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Asset Types list
        row = layout.row()

        row.template_list(
            "EXPORTER_UL_asset_types",
            "",
            scene,
            "exporter_asset_types",
            scene,
            "exporter_asset_type_index",
            rows=5,
        )

        column = row.column(align=True)

        column.operator(
            "exporter.asset_type_add",
            text="",
            icon="ADD",
        )

        column.operator(
            "exporter.asset_type_remove",
            text="",
            icon="REMOVE",
        )

        # Load / Save always visible
        layout.separator()

        row = layout.row(align=True)

        row.operator(
            "exporter.load_config",
            text="Load Config",
            icon="FILE_REFRESH",
        )

        row.operator(
            "exporter.save_config",
            text="Save Config",
            icon="FILE_TICK",
        )

        # Selected asset properties
        index = scene.exporter_asset_type_index

        if not (0 <= index < len(scene.exporter_asset_types)):
            return

        asset_type = scene.exporter_asset_types[index]

        layout.separator()

        # General
        box = layout.box()
        box.label(
            text="Asset Type",
            icon="ASSET_MANAGER",
        )

        box.prop(
            asset_type,
            "name_id",
        )

        box.prop(
            asset_type,
            "display_name",
        )

        # Naming
        naming_box = layout.box()
        naming_box.label(
            text="Naming Convention",
        )

        naming_box.prop(
            asset_type,
            "naming_prefix",
        )

        naming_box.prop(
            asset_type,
            "naming_suffix",
        )

        # Export Path
        path_box = layout.box()
        path_box.label(
            text="Export Path",
            icon="FILE_FOLDER",
        )

        path_box.prop(
            asset_type,
            "relative_path",
            text="Relative Path",
        )

        # Rules
        rules_box = layout.box()
        rules_box.label(
            text="Rules",
        )

        row = rules_box.row()

        row.template_list(
            "EXPORTER_UL_rules",
            "",
            asset_type,
            "rules",
            asset_type,
            "rule_index",
            rows=4,
        )

        buttons = row.column(align=True)

        buttons.operator(
            "exporter.rule_add",
            text="",
            icon="ADD",
        )

        buttons.operator(
            "exporter.rule_remove",
            text="",
            icon="REMOVE",
        )
