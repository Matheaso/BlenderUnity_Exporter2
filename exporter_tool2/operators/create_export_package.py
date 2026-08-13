import bpy

class EXPORTER_OT_CreateExportPackage(bpy.types.Operator):
    bl_idname = "exporter.create_export_package"
    bl_label = "Create Export Package"
    bl_description = "Create Export Package"

    def execute(self, context):

        obj = context.active_object
        if not obj:
            self.report({'ERROR'}, "No object selected")
            return {'CANCELLED'}

        collection = bpy.data.collections.new(obj.name)
        context.scene.collection.children.link(collection)

        for old_collection in list(obj.users_collection):
            if old_collection.name != collection:
                old_collection.objects.unlink(obj)

        collection.objects.link(obj)
        lod_collection = bpy.data.collections.new("LOD")
        collection.children.link(lod_collection)

        is_lod = context.scene.is_lod
        lod_num = context.scene.lod_number

        if is_lod:
            for i in range(lod_num):
                lod = obj.copy()
                lod.name = f"LOD{str(i)}_" + obj.name
                lod_collection.objects.link(lod)

        return {'FINISHED'}


#TODO: LOD0 is the main object so no need obj without LOD. Collection is enough


