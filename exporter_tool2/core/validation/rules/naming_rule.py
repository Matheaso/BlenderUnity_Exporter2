from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ..rule_interface import IValidationRule
from ..logging.validation_reporting import (
    ValidationIssue,
    ValidationReport,
)


class NameRule(IValidationRule):
    rule_id = "naming_rule"
    display_name = "Naming Convention"

    def validate(
        self,
        export_context: AssetPackage,
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