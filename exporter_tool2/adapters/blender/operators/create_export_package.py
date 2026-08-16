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
            self.report({'ERROR'}, "Selected object is already in Export Package")
            return {'CANCELLED'}

        collection = bpy.data.collections.new(f"EP_{obj.name}")
        collection.color_tag = "COLOR_03"
        context.scene.collection.children.link(collection)

        for old_collection in list(obj.users_collection):
            if old_collection.name != collection:
                old_collection.objects.unlink(obj)

        collection.objects.link(obj)

        return {'FINISHED'}


#TODO: LOD0 is the main object so no need obj without LOD. Collection is enough




def isAlreadyInValidCollection(obj) -> bool:
    for collection in obj.users_collection:
        if collection.name.startswith("EP_"):
            return True
        else:
            return False
