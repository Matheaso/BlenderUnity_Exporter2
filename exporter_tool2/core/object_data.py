import bpy
from dataclasses import dataclass


@dataclass(frozen=True)
class ObjectData:
    asset_name: str
    asset_type: str

    @property
    def is_mesh(self) -> bool:
        return self.asset_type == "MESH"



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


def create_export_context(blender_context: bpy.types.Context) -> ExportContext:

    objects = []

    for obj in blender_context.selected_objects:
        data = ObjectData(
            asset_name=obj.name,
            asset_type=obj.type,
        )
        objects.append(data)

    return ExportContext(tuple(objects), blender_context.active_object.name)
