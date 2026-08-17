from abc import ABC, abstractmethod
from typing import ClassVar

from .logging.validation_reporting import ValidationReport
from ..components import Component
from ..config_data import AssetTypeData
from ..asset_data import AssetPackage


class IValidationRule(ABC):
    rule_id: ClassVar[str]
    display_name: ClassVar[str]
    description: ClassVar[str]

    needed_components: ClassVar[tuple[type[Component], ...]] = ()

    @abstractmethod
    def validate(
            self,
            asset_package: AssetPackage,
            asset_type_data: AssetTypeData,
    )-> ValidationReport:
        issues = []

        return ValidationReport(
            issues=tuple(issues)
        )
