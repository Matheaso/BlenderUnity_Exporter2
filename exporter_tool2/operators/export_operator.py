import bpy

from ..validation.logging.validation_reporting import ValidationReport
from ..validation.logging.blender_report import BlenderValidationReporter
from ..core.config_data import AssetTypeData
from ..core.serialization import load_config
from ..validation.rule_registry import get_rule_class
from ..core.object_data import create_export_context


class EXPORT_TOOL_exporter(bpy.types.Operator):
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
        active_asset_type = get_active_asset_type(context)

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

        return {'FINISHED'}



def get_active_asset_type(context: bpy.types.Context) -> AssetTypeData:
    asset_types = load_config().asset_types
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
