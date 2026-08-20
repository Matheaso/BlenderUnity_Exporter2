import bpy

from exporter_tool2.adapters.blender.blender_adapter import BlenderAdapter
from exporter_tool2.adapters.blender.component_adapter import BlenderComponentAdapter
from exporter_tool2.adapters.blender.logging.blender_report import BlenderValidationReporter
from exporter_tool2.adapters.blender.operators.export_operator import get_active_asset_type
from exporter_tool2.core.serialization import load_config
from exporter_tool2.core.validation.logging.validation_reporting import ValidationReport
from exporter_tool2.core.validation.rule_registry import get_rule_class


class EXPORTER_OT_validation_test(bpy.types.Operator):
    bl_idname = "export.validate_operator"
    bl_label = "Validate Operator"
    bl_description = "Validate Operator"

    def execute(self, context: bpy.types.Context) -> bpy.types.Operator:
        self.report({'INFO'}, "Export Operator")

        all_issues = []

        selection = BlenderAdapter.get_selected_object(context.active_object)
        if not selection:
            self.report({'ERROR'}, "Select an object")
            return {"CANCELLED"}

        root = BlenderAdapter.get_export_package_from_selection(selection)

        if not root:
            self.report({'ERROR'}, "Couldn't find root object")
            return {"CANCELLED"}

        config = load_config()
        active_asset_type = get_active_asset_type(context, config)
        # BlenderAdapter.create_asset_package_from_selection(context)

        for rule_id in active_asset_type.rule_id:
            rule_class = get_rule_class(rule_id)
            rule = rule_class()

            objects = []

            for domain in rule.rule_domain:
                module = BlenderAdapter.get_module_from_root(root, domain)

                if module is not None:
                    objects.extend(module.children)

            asset_package = BlenderAdapter.create_asset_package(tuple(objects))

            for asset in asset_package.objects:
                blender_obj = bpy.data.objects.get(asset.name)

                for component_type in rule_class.needed_components:
                    new_comp = BlenderComponentAdapter.create_component(blender_obj, component_type)

                    asset.add_component(new_comp)

            report = rule.validate(asset_package, active_asset_type)
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
