from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar


class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

T = TypeVar("T")

@dataclass
class Result(Generic[T]):
    success: bool
    severity: Severity = Severity.INFO
    message: str = ""
    data: T | None = None
