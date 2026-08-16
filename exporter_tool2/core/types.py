from enum import Enum

class ObjectType(Enum):
    MESH = "MESH"
    EMPTY = "EMPTY"
    CURVE = "CURVE"
    OTHER = "OTHER"

class PackageObjectType(Enum):
    PACKAGE = 1
    MODULE = 2
    COLLISION = 3
    LOD = 4
    OCCLUDER = 5
