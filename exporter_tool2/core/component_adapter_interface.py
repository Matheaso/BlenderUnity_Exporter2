from abc import abstractmethod, ABC

from exporter_tool2.core.components import Component


class ComponentAdapterInterface(ABC):

    @staticmethod
    @abstractmethod
    def create_component(
            asset,
            component_type: type[Component]
    ) -> Component:
        pass