import bpy


class EXPORTER_OT_CreateExportPackage(bpy.types.Operator):
    bl_idname = "exporter.create_export_package"
    bl_label = "Create Export Package"
    bl_description = "Create Export Package"

    def execute(self, context):

        obj = context.active_object

        # TODO: One object for now, more later
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

        parent = bpy.data.objects.new("OBJECT", None)
        collection.objects.link(parent)

        parent.matrix_world.identity()

        for selected_obj in context.selected_objects:
            world_matrix = selected_obj.matrix_world.copy()

            selected_obj.parent = parent
            context.view_layer.update()
            selected_obj.matrix_world = world_matrix

        return {'FINISHED'}


def isAlreadyInValidCollection(obj) -> bool:
    for collection in obj.users_collection:
        if collection.name.startswith("EP_"):
            return True
        else:
            return False
