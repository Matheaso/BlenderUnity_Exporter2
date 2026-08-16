from enum import Enum

class ObjectType(Enum):
    MESH = "MESH"
    EMPTY = "EMPTY"
    CURVE = "CURVE"
    OTHER = "OTHER"

class PackageObjectType(Enum):
    PACKAGE = "PACKAGE"
    MODULE = "MODULE"
    COLLISION = "COLLISION"
    LOD = "LOD"
    OCCLUDER = "OCCLUDER"
