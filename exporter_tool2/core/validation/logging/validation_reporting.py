from dataclasses import dataclass
from enum import Enum, auto


class ValidationSeverity(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

@dataclass(frozen=True)
class ValidationIssue:
    message: str
    severity: ValidationSeverity

    @staticmethod
    def info(message: str) -> "ValidationIssue":
        return ValidationIssue(
            message=message,
            severity=ValidationSeverity.INFO
        )

    @staticmethod
    def warning(message: str) -> "ValidationIssue":
        return ValidationIssue(
            message=message,
            severity=ValidationSeverity.WARNING
        )

    @staticmethod
    def error(message: str) -> "ValidationIssue":
        return ValidationIssue(
            message=message,
            severity=ValidationSeverity.ERROR
        )


@dataclass(frozen=True)
class ValidationReport:
    issues: tuple[ValidationIssue, ...]

    @property
    def has_infos(self) -> bool:
        return any(
            issue.severity == ValidationSeverity.INFO
            for issue in self.issues
        )

    @property
    def has_errors(self) -> bool:
        return any(
            issue.severity == ValidationSeverity.ERROR
            for issue in self.issues
        )

    @property
    def has_warnings(self) -> bool:
        return any(
            issue.severity == ValidationSeverity.WARNING
            for issue in self.issues
        )

    @property
    def is_valid(self) -> bool:
        return not self.has_errors