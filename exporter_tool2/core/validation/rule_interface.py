from abc import ABC, abstractmethod
from typing import ClassVar

from .logging.validation_reporting import ValidationReport, ValidationIssue
from ..components import Component
from ..config_data import AssetTypeData
from ..asset_data import AssetPackage
from ..export_package import ExportPackage
from ..types import AssetDomain


class IValidationRule(ABC):
    rule_id: ClassVar[str]
    display_name: ClassVar[str]
    description: ClassVar[str] = ""

    needed_components: ClassVar[tuple[type[Component], ...]] = ()
    rule_domain: ClassVar[tuple[AssetDomain, ...]] = ()

    def __init__(self):
        self.issues = []

    def _begin_report(self):
        self.issues = []

    def _add_issue(self, issue: ValidationIssue):
        self.issues.append(issue)

    def _return_report(self) -> ValidationReport:
        return ValidationReport(
            issues=tuple(self.issues),
        )

    def _get_domain_objects(self, package: ExportPackage) -> AssetPackage:

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
