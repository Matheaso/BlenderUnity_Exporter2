import bpy

from ....validation.logging.validation_reporting import ValidationSeverity, ValidationReport

class BlenderValidationReporter:

    @staticmethod
    def report(
        operator: bpy.types.Operator,
        validation_report: ValidationReport,
    ) -> None:

        for issue in validation_report.issues:
            if issue.severity == ValidationSeverity.ERROR:
                report_type = {"ERROR"}

            elif issue.severity == ValidationSeverity.WARNING:
                report_type = {"WARNING"}

            else:
                report_type = {"INFO"}

            operator.report(
                report_type,
                issue.message
            )