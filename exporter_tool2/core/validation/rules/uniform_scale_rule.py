from ..logging.validation_reporting import (
    ValidationReport,
    ValidationIssue,
    ValidationSeverity
)
from ...components import Transform
from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ...validation.rule_interface import IValidationRule

class UniformScale(IValidationRule):
    rule_id = "uniform_scale"
    display_name = "Uniform Scale"
    description = ("Rule:\n"
                   "- Scale needs to be applied)\n"
                   )

    needed_components = (Transform,)

    def validate(
            self,
            asset_package: AssetPackage,
            asset_type_data: AssetTypeData
    ) -> ValidationReport:
        issues = []

        for obj_data in asset_package.objects:

            transform = obj_data.get_component(Transform)

            if transform is None:
                issues.append(
                    ValidationIssue(
                        f"Asset without Transform component: {obj_data.name}",
                        ValidationSeverity.ERROR,
                    )
                )
                continue
            else:
                issues.append(ValidationIssue(
                    "WORKING: Transform is NOT null",
                    ValidationSeverity.INFO,
                ))

            if not transform.is_scale_identity():
                issues.append(
                    ValidationIssue(
                        f"{obj_data.name}: Has scale different than identity. Apply scale to continue.",
                        ValidationSeverity.ERROR,
                    )
                )

        return ValidationReport(
            issues=tuple(issues)
        )

