from dataclasses import dataclass
from typing import TypeVar

from exporter_tool2.core.components import Component
from exporter_tool2.core.types import ObjectType

float3 = tuple[float, float, float]

T = TypeVar('T', bound=Component)


class AssetData:
    name: str
    object_type: ObjectType
    components: list[Component]

    def to_view(self) -> AssetDataView:
        return AssetDataView(
            name=self.name,
            object_type=self.object_type,
            components=tuple(self.components)
        )

    def is_mesh(self) -> bool:
        return self.object_type == ObjectType.MESH

    def add_component(self, component: T):
        for component in self.components:
            if isinstance(component, type(component)):
                return

        self.components.append(component)

    def get_component(self, component_type: type[T]) -> T | None:
        for component in self.components:
            if isinstance(component, type(component_type)):
                return component
        return None

    # TODO: probably no need for this
    def get_or_create_component(self, component: T) -> T:
        existing = self.get_component(type(component))
        if existing:
            return existing

        self.add_component(component)
        return component


# Not mutable AssetData type
@dataclass(frozen=True)
class AssetDataView:
    name: str
    object_type: ObjectType
    components: tuple[Component, ...]


@dataclass(frozen=True)
class AssetPackage:
    objects: tuple[AssetData, ...]
    active_object_name: str

    @property
    def mesh_objects(self) -> tuple[AssetData, ...]:

        result = []
        for obj in self.objects:
            if obj.is_mesh:
                result.append(obj)

        return tuple(result)

    @property
    def is_empty(self) -> bool:
        return len(self.objects) == 0
