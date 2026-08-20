from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ..rule_interface import IValidationRule
from ..logging.validation_reporting import (
    ValidationIssue,
    ValidationReport,
)
from ...types import AssetDomain


class COLNamingRule(IValidationRule):
    rule_id = "col_naming_rule"
    display_name = "Collision Naming Base"
    description = "Collision prefix: 'COL_'"

    needed_components = ()
    rule_domain = (AssetDomain.COLLISION,)

    def validate(
            self,
            asset_package: AssetPackage,
            asset_type_data: AssetTypeData,
    ) -> ValidationReport:

        self._begin_report()

        self._add_issue(
            ValidationIssue.info(f"COLNamingRule started...")
        )

        col_prefix = "COL_"

        for obj_context in asset_package.objects:
            if not obj_context.name.startswith(col_prefix):
                self._add_issue(
                    ValidationIssue.error(f"Object '{obj_context.name}' must start with '{col_prefix}'.")
                )

        return self._return_report()
