import bpy

from exporter_tool2.adapters.blender.operators import EXPORTER_OT_lod_module_switch, EXPORTER_OT_collision_module_switch
from exporter_tool2.adapters.blender.operators.collision_shape_operators import (
    EXPORTER_OT_create_collision_shape
)
from exporter_tool2.adapters.blender.operators import (
    EXPORTER_OT_CreateExportPackage
)
from exporter_tool2.adapters.blender.tools.bl_suffixer import (
    SUFFIXER_OT_prefix, SUFFIXER_OT_replace, SUFFIXER_OT_suffix, SUFFIXER_OT_auto
)
from exporter_tool2.adapters.blender.operators.export_operator import (
    EXPORTER_OT_exporter
)


class EXPORTER_PT_sidebar(bpy.types.Panel):
    bl_idname = "exporter.sidebar"
    bl_label = "EXPORT"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exporter"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            EXPORTER_OT_exporter.bl_idname,
            text="Export selected",
        )


class EXPORTER_PT_Temp(bpy.types.Panel):
    bl_idname = "exporter.temp"
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
    bl_idname = "exporter.main_settings"
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







