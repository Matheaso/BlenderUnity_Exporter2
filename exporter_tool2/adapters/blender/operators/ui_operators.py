import bpy

from exporter_tool2.adapters.blender.blender_adapter import BlenderAdapter
from exporter_tool2.core.types import PackageObjectType


# TODO: Should be from selection ExportPackage context
# Is is intended to not destroy LOD na Collision collection on "disable LOD"
# it prevents mistakes, you can always delete it manualy.
# importer should be aware that empty LOD means no LOD

class EXPORTER_OT_collision_module_switch(bpy.types.Operator):
    bl_idname = "exporter.collision_module_switch"
    bl_label = "Export Selected Collision Module"

    def execute(self, context):
        export_collection = BlenderAdapter.get_export_package_from_selection(context.active_object)
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_collision = not context.scene.is_collision

        if context.scene.is_collision:
            if not BlenderAdapter.get_module_from_root(export_collection, PackageObjectType.COLLISION):
                new_object = bpy.data.objects.new(PackageObjectType.COLLISION.value, None)
                export_collection.objects.link(new_object)

        BlenderAdapter.create_export_package()
        return {'FINISHED'}

# TODO: Change from collection to object
class EXPORTER_OT_lod_module_switch(bpy.types.Operator):
    bl_idname = "exporter.lod_module_switch"
    bl_label = "Export Selected LOD Module"

    def execute(self, context):
        export_collection = BlenderAdapter.get_export_package_from_selection(context.active_object)
        if not export_collection:
            return {'CANCELLED'}

        context.scene.is_lod = not context.scene.is_lod

        if context.scene.is_lod:
            if not BlenderAdapter.get_module_from_root(export_collection, PackageObjectType.LOD):
                lod_collection = bpy.data.collections.new("LOD")
                lod_collection.color_tag = "COLOR_03"
                export_collection.children.link(lod_collection)

        return {'FINISHED'}

