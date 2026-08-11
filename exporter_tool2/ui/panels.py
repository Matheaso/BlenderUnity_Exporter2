import bpy

from ..tools.suffixer import SUFFIXER_OT_prefix, SUFFIXER_OT_replace, SUFFIXER_OT_suffix, SUFFIXER_OT_auto
from ..operators.export_operator import EXPORT_TOOL_exporter


class EXPORTERTOOL_PT_sidebar(bpy.types.Panel):
    bl_idname = "EXPORT_TOOL2_PT_sidebar"
    bl_label = "EXPORT"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            EXPORT_TOOL_exporter.bl_idname,
            text="Export selected",
        )




class EXPORTERTOOL_PT_main_settings(bpy.types.Panel):
    bl_idname = "EXPORTERTOOL_PT.main_settings"
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
    bl_idname = "suffixer.main_panel"
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







