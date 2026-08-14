import bpy

from exporter_tool2.core.types import ObjectType
from exporter_tool2.core.object_data import ExportContext, ObjectData
from exporter_tool2.config.helpers import get_asset_types


def get_blender_asset_types(self, context):
    return get_asset_types()


def create_export_context(blender_context: bpy.types.Context) -> ExportContext:
    objects = []
    for obj in blender_context.selected_objects:
        data = ObjectData(
            asset_name=obj.name,
            asset_type=ObjectType(obj.type),
            pivot_location=tuple(obj.location),
            scale=tuple(obj.scale),
        )
        objects.append(data)
    return ExportContext(tuple(objects), blender_context.active_object.name)


def find_export_package_from_selection():
    selection = bpy.context.active_object

    for col in selection.users_collection:
        if col.name.startswith("EP_"):
            return col
    return None


def is_col_exist(col_name: str):
        selection = bpy.context.active_object
        export_package = None

        for col in selection.users_collection:
            if col.name.startswith("EP_"):
                export_package = col

        if export_package:
            for col in selection.users_collection:
                if col.name == col_name:
                    return True
        else:
            return False