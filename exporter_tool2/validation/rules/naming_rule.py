from ..logging.validation_reporting import ValidationReport
from ...core.config_data import AssetTypeData
from ...core.object_data import ExportContext
from ...validation.rule_interface import IValidationRule

class NameRule(IValidationRule):
    rule_id = "naming_rule"
    display_name = "Naming Convention"
    description = ("Rule:\n"
                   "- Needs proper prefixes and suffixes\n"
                   "- Can't have default blender name"
                   )

    def validate(
            self,
            export_context: ExportContext,
            asset_type_data: AssetTypeData
    ) -> ValidationReport:
        issues = []

        return ValidationReport(
            issues=tuple(issues)
        )
