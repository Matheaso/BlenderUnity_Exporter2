import bpy

from exporter_tool2.core.object_data import ObjectData, ExportContext

def create_export_context(blender_context: bpy.types.Context) -> ExportContext:
    objects = []

    for obj in blender_context.selected_objects:
        data = ObjectData(
            asset_name=obj.name,
            asset_type=obj.type,
            pivot_location=tuple(obj.location),
            scale=tuple(obj.scale),
        )
        objects.append(data)

    return ExportContext(tuple(objects), blender_context.active_object.name)
