import bpy

from exporter_tool2.adapters.blender.operators import EXPORTER_OT_lod_module_switch, \
    EXPORTER_OT_collision_module_switch, EXPORTER_OT_validation_test, EXPORT_OT_export_collection_operator

from exporter_tool2.adapters.blender.operators import (
    EXPORTER_OT_CreateExportPackage
)
from exporter_tool2.adapters.blender.modules.bl_suffixer import (
    SUFFIXER_OT_prefix, SUFFIXER_OT_replace, SUFFIXER_OT_suffix, SUFFIXER_OT_auto
)



class EXPORTER_PT_sidebar(bpy.types.Panel):
    bl_idname = "EXPORTER_PT_Sidebar"
    bl_label = "EXPORT"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            EXPORT_OT_export_collection_operator.bl_idname,
            text="Export selected",
        )

        layout.operator(
            EXPORTER_OT_validation_test.bl_idname,
            text="[ Validation Test ]",
        )


class EXPORTER_PT_Temp(bpy.types.Panel):
    bl_idname = "EXPORTER_PT_Temp"
    bl_label = "Export Package"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            EXPORTER_OT_CreateExportPackage.bl_idname,
            text="Create Export Package",
        )

        if not context.scene.is_lod:
            layout.operator(
                EXPORTER_OT_lod_module_switch.bl_idname,
                text="Enable LOD"
            )

        if not context.scene.is_collision:
            layout.operator(
                EXPORTER_OT_collision_module_switch.bl_idname,
                text="Enable Collision"
            )


class EXPORTER_PT_main_settings(bpy.types.Panel):
    bl_idname = "EXPORTER_PT_Main_settings"
    bl_label = "Main Settings"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.export_settings

        layout.label(text="Asset Type")

        layout.prop(
            settings,
            "asset_type",
            text=""
        )


class SUFFIXER_PT_main_settings(bpy.types.Panel):
    bl_idname = "EXPORTER_PT_Main_panel"
    bl_label = "Suffixer"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)

        row.operator(
            SUFFIXER_OT_prefix.bl_idname,
            text="Pre_",
        )

        row.operator(
            SUFFIXER_OT_replace.bl_idname,
            text="Replace",
        )

        row.operator(
            SUFFIXER_OT_suffix.bl_idname,
            text="_Suff",
        )

        layout.operator(
            SUFFIXER_OT_auto.bl_idname,
            text="Auto",
        )
