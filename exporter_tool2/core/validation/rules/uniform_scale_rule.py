from ..logging.validation_reporting import (
    ValidationReport,
    ValidationIssue,
    ValidationSeverity
)
from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ...validation.rule_interface import IValidationRule

class UniformScale(IValidationRule):
    rule_id = "uniform_scale"
    display_name = "Uniform Scale"
    description = ("Rule:\n"
                   "- Scale needs to be applied)\n"
                   )

    def validate(
            self,
            export_context: AssetPackage,
            asset_type_data: AssetTypeData
    ) -> ValidationReport:
        issues = []

        for obj_data in export_context.objects:
            if not obj_data.is_uniform_scale:
                issues.append(
                    ValidationIssue(
                        f"{obj_data.asset_name}: Has non uniform scale. Apply scale to continue",
                        ValidationSeverity.ERROR
                    )
                )
        return ValidationReport(
            issues=tuple(issues)
        )

