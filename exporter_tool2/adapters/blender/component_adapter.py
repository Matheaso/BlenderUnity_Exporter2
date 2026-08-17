import bpy

from exporter_tool2.core.components import Component
from exporter_tool2.core.component_adapter_interface import ComponentAdapterInterface
from exporter_tool2.core.components import Transform


class BlenderComponentAdapter(ComponentAdapterInterface):

    @staticmethod
    def create_component(obj: bpy.types.Object, component_type: type[Component]) -> Component:

        factory = BlenderComponentAdapter._component_factories.get(component_type)

        if factory is None:
            raise ValueError(
                f"Unsupported component: {component_type.__name__}"
            )

        return factory(obj)

    @staticmethod
    def create_transform_component(obj: bpy.types.Object) -> Transform:
        return Transform(
            translation=tuple(obj.location),
            rotation=tuple(obj.rotation_euler),
            scale=tuple(obj.scale),
            pivot=tuple(obj.matrix_world.translation),
        )


BlenderComponentAdapter._component_factories = {
    Transform: BlenderComponentAdapter.create_transform_component,
}