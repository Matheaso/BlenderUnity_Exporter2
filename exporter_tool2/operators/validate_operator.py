from pathlib import Path

import bpy

from ..core.asset_type_data import NamingConvention
from ..core import serialization
from ..core.asset_type_data import AssetTypeData, ExporterConfigData
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


class EXPORT_TOOL_test(bpy.types.Operator):
    bl_idname = "export.test"
    bl_label = "test Operator"
    bl_description = "test Operator"

    def execute(self, context):
        self.report({'INFO'}, "test Operator")

        assets = (
            AssetTypeData(
                "01",
                "DisplayName_1",
                NamingConvention(
                    "",
                    "",
                ),
                ("",)
            ),
            AssetTypeData(
                "02",
                "DisplayName_2",
                NamingConvention(
                    "SM_",
                    "",
                ),
                ("",)
            )
        )

        config = ExporterConfigData(
            Path(__file__).parent.parent,
            assets,
        )

        serialization.save_config(config)

        return {'FINISHED'}
