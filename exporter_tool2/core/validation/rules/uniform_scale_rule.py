from ..logging.validation_reporting import (
    ValidationReport,
    ValidationIssue,
)
from ...components import Transform
from ...config_data import AssetTypeData
from ...asset_data import AssetPackage
from ...validation.rule_interface import IValidationRule

class IdentityScale(IValidationRule):
    rule_id = "identity_scale"
    display_name = "Identity Scale"
    description = ("Rule:\n"
                   "- Scale needs to be applied)\n"
                   )

    needed_components = (Transform,)

    def validate(
            self,
            asset_package: AssetPackage,
            asset_type_data: AssetTypeData
    ) -> ValidationReport:

        self._begin_validation()

        for obj_data in asset_package.objects:
            transform = obj_data.get_component(Transform)

            if not transform.is_scale_identity():
                self._add_issue(
                    ValidationIssue.error(
                        f"{obj_data.name}: Has scale different than identity. Apply scale to continue."
                    )
                )

        return self._return_report()

