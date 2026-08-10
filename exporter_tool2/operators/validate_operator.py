import bpy
from ..core.object_data import create_export_context, ExportContext


class EXPORT_TOOL_validate(bpy.types.Operator):
    bl_idname = "export.validate"
    bl_label = "Validate Operator"
    bl_description = "Validate Operator"

    def execute(self, context):
        self.report({'INFO'}, "Validate Operator")

        export_context = create_export_context(context)

        asset_type  = context.scene.export_settings.asset_type

        self.report({'WARNING'}, asset_type)

        for obj in export_context.mesh_objects:
            if obj.asset_type == 'MESH':
                self.report({'INFO'}, "IT IS MESH")
            else:
                self.report({'WARNING'}, "IT IS NOT MESH")

        return {'FINISHED'}

