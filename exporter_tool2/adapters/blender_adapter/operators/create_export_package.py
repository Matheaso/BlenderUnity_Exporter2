import bpy

class EXPORTER_OT_CreateExportPackage(bpy.types.Operator):
    bl_idname = "exporter.create_export_package"
    bl_label = "Create Export Package"
    bl_description = "Create Export Package"

    def execute(self, context):

        obj = context.active_object

        #TODO: It is a guard for now, later it should be possible to put more
        # than one object into export package
        if len(context.selected_objects) > 1:
            self.report({'ERROR'}, "Select one object")
            return {'CANCELLED'}

        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "No mesh object selected")
            return {'CANCELLED'}

        if isAlreadyInValidCollection(obj):
            self.report({'ERROR'}, "Collection already exists")
            return {'CANCELLED'}

        collection = bpy.data.collections.new(f"EP_{obj.name}")
        context.scene.collection.children.link(collection)

        for old_collection in list(obj.users_collection):
            if old_collection.name != collection:
                old_collection.objects.unlink(obj)

        collection.objects.link(obj)
        lod_collection = bpy.data.collections.new("LOD")
        collection.children.link(lod_collection)


        #TODO: This sections are temp, their place is in dynamic window with poll()

        # LOD Section #
        lod_num = context.scene.lod_number

        if context.scene.is_lod:
            for i in range(lod_num):
                lod = obj.copy()
                lod.name = f"LOD{str(i)}_" + obj.name
                lod_collection.objects.link(lod)


        # Collision Section #
        collision_collection = bpy.data.collections.new("Collision")
        collection.children.link(collision_collection)



        return {'FINISHED'}






#TODO: LOD0 is the main object so no need obj without LOD. Collection is enough




def isAlreadyInValidCollection(obj) -> bool:
    for collection in obj.users_collection:
        if collection.name == obj.name:
            return True
        else:
            return False
