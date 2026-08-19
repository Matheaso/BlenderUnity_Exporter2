from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ..rule_interface import IValidationRule
from ..logging.validation_reporting import (
    ValidationIssue,
    ValidationReport,
)
from ...types import AssetDomain


class NameRule(IValidationRule):
    rule_id = "naming_rule"
    display_name = "Naming Convention"
    description = "Naming convention"

    needed_components = ()
    rule_domain = (AssetDomain.OBJECT)

    def validate(
        self,
        asset_package: AssetPackage,
        asset_type_data: AssetTypeData,
    ) -> ValidationReport:

        issues = []

        naming = asset_type_data.naming_convention

        for obj_context in asset_package.objects:
            if naming.prefix and not obj_context.name.startswith(naming.prefix):
                issues.append(
                    ValidationIssue.error(
                        f"Object '{obj_context.name}' must start with '{naming.prefix}'."
                    )
                )

            if naming.suffix and not obj_context.name.endswith(naming.suffix):
                issues.append(
                    ValidationIssue.error(
                        f"Object '{obj_context.name}' must end with '{naming.suffix}'."
                    )
                )

        return ValidationReport(
            issues=tuple(issues)
        )