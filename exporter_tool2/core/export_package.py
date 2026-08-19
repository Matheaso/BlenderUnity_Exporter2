from dataclasses import dataclass
from exporter_tool2.core.types import AssetDomain


@dataclass(frozen=True)
class PackageNode:
    name: str
    parent: AssetDomain


@dataclass(frozen=True)
class ExportPackage:
    root_name: str
    nodes: tuple[PackageNode, ...]

    @property
    def get_object(self, name: str) -> PackageNode | None:
        for node in self.nodes:
            if node.name == name:
                return node
        return None


