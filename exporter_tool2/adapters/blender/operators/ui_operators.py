import bpy

from exporter_tool2.adapters.blender.helpers import (
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
        export_collection = find_export_package_from_selection()
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_collision = not context.scene.is_collision

        if context.scene.is_collision:
            if not is_col_exist("Collision"):
                collision_collection = bpy.data.collections.new("Collision")
                collision_collection.color_tag = "COLOR_03"
                export_collection.children.link(collision_collection)

        return {'FINISHED'}


class EXPORTER_OT_lod_module_switch(bpy.types.Operator):
    bl_idname = "exporter.lod_module_switch"
    bl_label = "Export Selected LOD Module"

    def execute(self, context):
        export_collection = find_export_package_from_selection()
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_lod = not context.scene.is_lod

        if context.scene.is_lod:
            if not is_col_exist("LOD"):
                lod_collection = bpy.data.collections.new("LOD")
                lod_collection.color_tag = "COLOR_03"
                export_collection.children.link(lod_collection)

        return {'FINISHED'}

