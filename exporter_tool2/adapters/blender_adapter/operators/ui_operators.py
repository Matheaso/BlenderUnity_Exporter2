import bpy

class EXPORTER_OT_collision_module_switch(bpy.types.Operator):
    bl_idname = "exporter.collision_module_switch"
    bl_label = "Export Selected Collision Module"

    def execute(self, context):
        context.scene.is_collision = not context.scene.is_collision

        return {'FINISHED'}


class EXPORTER_OT_lod_module_switch(bpy.types.Operator):
    bl_idname = "exporter.lod_module_switch"
    bl_label = "Export Selected LOD Module"

    def execute(self, context):
        context.scene.is_lod = not context.scene.is_lod

        return {'FINISHED'}
