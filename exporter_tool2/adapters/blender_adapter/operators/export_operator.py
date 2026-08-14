import bpy

from exporter_tool2.core.validation.logging.validation_reporting import ValidationReport
from exporter_tool2.adapters.blender_adapter.helpers import create_export_context
from exporter_tool2.core.config_data import ExporterConfigData
from exporter_tool2.core.serialization import load_config
from exporter_tool2.core.config_data import AssetTypeData
from exporter_tool2.core.validation.rule_registry import get_rule_class
from exporter_tool2.adapters.blender_adapter.logging.blender_report import BlenderValidationReporter


class EXPORTER_OT_exporter(bpy.types.Operator):
    bl_label = "Export Selected"
    bl_idname = "export.export_selected"
    bl_description = "Export Selected objects"

    def execute(self, context):
        self.report({'INFO'}, "Export Operator")

        all_issues = []

        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'FINISHED'}

        export_context = create_export_context(context)
        config = load_config()
        active_asset_type = get_active_asset_type(context, config)

        for rule_id in active_asset_type.rule_id:
            rule_class = get_rule_class(rule_id)
            rule = rule_class()

            report = rule.validate(export_context, active_asset_type)
            all_issues.extend(report.issues)

        validation_report = ValidationReport(
            issues=tuple(all_issues)
        )

        BlenderValidationReporter.report(
            self,
            validation_report,
        )

        if not validation_report.is_valid:
            self.report({'ERROR'}, "Export failed")
            return {"CANCELLED"}

        ## EXPORT ##

        export_dir = (
                config.project_dir
                / active_asset_type.relative_path
        )

        export_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = context.selected_objects[0].name
        filepath = export_dir / f"{filename}.fbx"

        bpy.ops.export_scene.fbx(
            filepath=str(filepath),
            use_selection=True,
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_ALL",
            axis_forward="-Z",
            axis_up="Y",
            add_leaf_bones=False,
            bake_anim=False,
            use_space_transform=True,
            bake_space_transform=True,
        )

        self.report(
            {"INFO"},
            f"Exported to: {filepath}",
        )

        return {'FINISHED'}



def get_active_asset_type(context: bpy.types.Context, config: ExporterConfigData) -> AssetTypeData:
    asset_types = config.asset_types
    asset_type_id = context.scene.export_settings.asset_type

    asset_type = next(
        (
            asset_type
            for asset_type in asset_types
            if asset_type.name_id == asset_type_id
        ),
        None
    )
    if not asset_type:
        raise RuntimeError("Couldn't find active asset type")
    return asset_type
