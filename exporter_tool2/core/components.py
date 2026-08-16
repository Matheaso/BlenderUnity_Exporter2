from abc import ABC
from dataclasses import dataclass

Float3 = tuple[float, float, float]

class Component(ABC):
    pass


@dataclass(frozen=True)
class Transform(Component):
    translation: Float3
    rotation: Float3
    scale: Float3
    pivot: Float3

    def is_scale_identity(self) -> bool:
        return self.scale == (1.0, 1.0, 1.0)

    def is_pivot_zeroed(self) -> bool:
        return self.pivot == (0, 0, 0)

    def is_rotation_zeroed(self) -> bool:
        return self.rotation == (0, 0, 0)