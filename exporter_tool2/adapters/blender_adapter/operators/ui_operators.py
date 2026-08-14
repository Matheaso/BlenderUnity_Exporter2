import bpy

from exporter_tool2.adapters.blender_adapter.helpers import (
    find_export_package_from_selection,
    is_col_exist,

)


# Is is intended to not destroy LOD na Collision collection on "disable LOD"
# it prevents mistakes, you can always delete it manualy.
# importer should be aware that empty LOD means no LOD

class EXPORTER_OT_collision_module_switch(bpy.types.Operator):
    bl_idname = "exporter.collision_module_switch"
    bl_label = "Export Selected Collision Module"

    def execute(self, context):
        export_collection = find_export_package_from_selection(context)
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_collision = not context.scene.is_collision

        if context.scene.is_collision:
            if not is_col_exist(context, "Collision"):
                collision_collection = bpy.data.collections.new("Collision")
                collision_collection.color_tag = "COLOR_03"
                export_collection.children.link(collision_collection)

        return {'FINISHED'}


class EXPORTER_OT_lod_module_switch(bpy.types.Operator):
    bl_idname = "exporter.lod_module_switch"
    bl_label = "Export Selected LOD Module"

    def execute(self, context):
        export_collection = OPHelper.find_export_package_from_selection(context)
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_lod = not context.scene.is_lod

        if context.scene.is_lod:
            if not OPHelper.is_col_exist(context, "LOD"):
                lod_collection = bpy.data.collections.new("LOD")
                lod_collection.color_tag = "COLOR_03"
                export_collection.children.link(lod_collection)

        return {'FINISHED'}


# def find_export_package_from_selection(context):
#     selection = bpy.context.active_object
#
#     for col in selection.users_collection:
#         if col.name.startswith("EP_"):
#             return col
#
#     return None
#
# def is_col_exist(context, col_name: str):
#     selection = bpy.context.active_object
#     export_package = None
#
#     for col in selection.users_collection:
#         if col.name.startswith("EP_"):
#             export_package = col
#
#     if export_package:
#         for col in selection.users_collection:
#             if col.name == col_name:
#                 return True
#     else:
#         return False
