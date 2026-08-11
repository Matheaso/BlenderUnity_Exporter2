from ...core.config_data import AssetTypeData
from ...core.object_data import ExportContext
from ...validation.rule_interface import IValidationRule
from ...validation.logging.validation_reporting import (
    ValidationIssue,
    ValidationReport,
)


class NameRule(IValidationRule):
    rule_id = "naming_rule"
    display_name = "Naming Convention"

    def validate(
        self,
        export_context: ExportContext,
        asset_type_data: AssetTypeData,
    ) -> ValidationReport:

        issues = []

        naming = asset_type_data.naming_convention

        for obj_context in export_context.objects:
            if naming.prefix and not obj_context.asset_name.startswith(naming.prefix):
                issues.append(
                    ValidationIssue.error(
                        f"Object '{obj_context.asset_name}' must start with '{naming.prefix}'."
                    )
                )

            if naming.suffix and not obj_context.asset_name.endswith(naming.suffix):
                issues.append(
                    ValidationIssue.error(
                        f"Object '{obj_context.asset_name}' must end with '{naming.suffix}'."
                    )
                )

        return ValidationReport(
            issues=tuple(issues)
        )