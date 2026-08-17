from abc import ABC, abstractmethod
from typing import ClassVar

from .logging.validation_reporting import ValidationReport, ValidationIssue
from ..components import Component
from ..config_data import AssetTypeData
from ..asset_data import AssetPackage


class IValidationRule(ABC):
    rule_id: ClassVar[str]
    display_name: ClassVar[str]
    description: ClassVar[str] = ""

    needed_components: ClassVar[tuple[type[Component], ...]] = ()

    def __init__(self):
        self.issues = []

    def _begin_validation(self):
        self.issues = []

    def _add_issue(self, issue: ValidationIssue):
        self.issues.append(issue)

    def _return_report(self):
        ValidationReport(
            issues=tuple(self.issues),
        )

    @abstractmethod
    def validate(
            self,
            asset_package: AssetPackage,
            asset_type_data: AssetTypeData,
    )-> ValidationReport:
        self.issues = []

        return ValidationReport(
            issues=tuple(self.issues)
        )
