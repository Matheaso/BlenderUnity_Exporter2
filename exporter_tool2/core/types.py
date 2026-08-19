from enum import Enum

class ObjectType(Enum):
    MESH = "MESH"
    EMPTY = "EMPTY"
    CURVE = "CURVE"
    OTHER = "OTHER"

class AssetDomain(Enum):
    PACKAGE = "PACKAGE"
    OBJECT = "OBJECT"
    COLLISION = "COLLISION"
    LOD = "LOD"
    OCCLUDER = "OCCLUDER"
    SKELETON = "SKELETON"
