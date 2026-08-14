import bpy

from exporter_tool2.adapters.blender_adapter.operators import (
    EXPORTER_OT_create_collision_shape,
    EXPORTER_OT_collision_module_switch
)
from exporter_tool2.adapters.blender_adapter.operators import (
    EXPORTER_OT_lod_module_switch
)


class EXPORTER_PT_lod_module(bpy.types.Panel):
    bl_idname = "exporter.lod_module"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "LOD"
    bl_category = "Exporter"

    @classmethod
    def poll(cls, context):
        return context.scene.is_lod

    def draw(self, context):
        layout = self.layout

        layout.prop(
            context.scene,
            "lod_number",
        )

        spacer_row = layout.row()
        spacer_row.separator(factor=2)

        red_row = layout.row()
        red_row.alert = True
        red_row.operator(
            EXPORTER_OT_lod_module_switch.bl_idname,
            text="Disable LOD"
        )

class EXPORTER_PT_collision_module(bpy.types.Panel):
    bl_idname = "exporter.collision_module"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Collision"
    bl_category = "Exporter"

    @classmethod
    def poll(cls, context):
        return context.scene.is_collision

    def draw(self, context):
        layout = self.layout
        layout.label(text="Create Collision Shape")

        collision_row = layout.row(align=True)
        collision_row_2 = layout.row(align=True)

        op = collision_row.operator(
            EXPORTER_OT_create_collision_shape.bl_idname,
            icon="CUBE",
            text="Cube",
        )
        op.shape_type = "CUBE"

        op = collision_row.operator(
            EXPORTER_OT_create_collision_shape.bl_idname,
            icon="SPHERE",
            text="Sphere",
        )
        op.shape_type = "SPHERE"

        op = collision_row_2.operator(
            EXPORTER_OT_create_collision_shape.bl_idname,
            text="Capsule",
        )
        op.shape_type = "CAPSULE"

        op = collision_row_2.operator(
            EXPORTER_OT_create_collision_shape.bl_idname,
            text="Convex",
        )
        op.shape_type = "CONVEX"

        spacer_row = layout.row()
        spacer_row.separator(factor=2)

        red_row = layout.row()
        red_row.alert = True
        red_row.operator(
            EXPORTER_OT_collision_module_switch.bl_idname,
            text="Disable Collision"
        )