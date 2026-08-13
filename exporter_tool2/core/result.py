from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

T = TypeVar("T")

@dataclass(frozen=True)
class Result(Generic[T]):
    success: bool
    severity: Severity = Severity.INFO
    message: str = ""
    data: T | None = None

    @staticmethod
    def ok(data: T | None = None, message: str = ""):
        return Result(
            success=True,
            severity=Severity.INFO,
            message=message,
            data=data
        )

    @staticmethod
    def error(message: str):
        return Result(
            success=False,
            severity=Severity.ERROR,
            message=message,
        )

    @staticmethod
    def warning(message: str):
        return Result(
            success=False,
            severity=Severity.WARNING,
            message=message,
        )