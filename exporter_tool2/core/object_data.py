import bpy
from dataclasses import dataclass

from ..core.types import ObjectType

float3 = tuple[float, float, float]

@dataclass(frozen=True)
class ObjectData:
    asset_name: str
    asset_type: ObjectType
    pivot_location: float3
    scale: float3

    @property
    def is_mesh(self) -> bool:
        return self.asset_type == ObjectType.MESH

    @property
    def is_pivot_zeroed(self) -> bool:
        return  self.pivot_location == (0.0, 0.0, 0.0)

    @property
    def is_uniform_scale(self) -> bool:
        return self.scale == (1.0, 1.0, 1.0)


@dataclass(frozen=True)
class ExportContext:
    objects: tuple[ObjectData, ...]
    active_object_name: str

    @property
    def mesh_objects(self) -> tuple[ObjectData, ...]:

        result = []
        for obj in self.objects:
            if obj.is_mesh:
                result.append(obj)

        return tuple(result)

    @property
    def is_empty(self) -> bool:
        return len(self.objects) == 0


