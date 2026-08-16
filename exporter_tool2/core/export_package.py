from dataclasses import dataclass
from enum import Enum


class PackageObjectType(Enum):
    PACKAGE = 1
    MODULE = 2
    COLLISION = 3
    LOD = 4
    OCCLUDER = 5

@dataclass(frozen=True)
class PackageNode:
    name: str
    root: str
    type: PackageObjectType

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




