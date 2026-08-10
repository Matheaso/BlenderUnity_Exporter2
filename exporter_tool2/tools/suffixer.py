import bpy

from ..core.config_data import NamingConvention
from ..core.serialization import load_config


class SUFFIXER_OT_suffix(bpy.types.Operator):
    bl_idname = "suffixer.suffix"
    bl_label = "suffix Operator"
    bl_description = "Suffix Operator"

    suffix: bpy.props.StringProperty(
        name="Replace from",
        default="",
    )

    def invoke(self, context, event):
        if not context.selected_objects:
            return {'CANCELLED'}
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):

        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'FINISHED'}

        if not self.suffix:
            return {'CANCELLED'}

        objects = bpy.context.selected_objects

        self.suffix = self.suffix.replace("_", "")

        for obj in objects:
            if not obj.name.endswith("_"):
                obj.name += "_"
            obj.name += f"{self.suffix}"


        return {'FINISHED'}


class SUFFIXER_OT_prefix(bpy.types.Operator):
    bl_idname = "suffixer.prefix"
    bl_label = "prefix Operator"
    bl_description = "Prefix Operator"

    prefix: bpy.props.StringProperty(
        name="Replace from",
        default="",
    )

    def invoke(self, context, event):
        if not context.selected_objects:
            return {'CANCELLED'}
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'FINISHED'}

        if not self.prefix:
            return {'CANCELLED'}

        objects = bpy.context.selected_objects

        self.prefix = self.prefix.replace("_", "")

        for obj in objects:
            if not obj.name.startswith("_"):
                obj.name = "_" + obj.name

            obj.name = f"{self.prefix}{obj.name}"

        return {'FINISHED'}


class SUFFIXER_OT_replace(bpy.types.Operator):
    bl_idname = "suffixer.replace"
    bl_label = "replace Operator"
    bl_description = "Replace Operator"

    replace_from: bpy.props.StringProperty(
        name="Replace from",
        default="",
    )

    replace_to: bpy.props.StringProperty(
        name="Replace to",
        default="",
    )

    def invoke(self, context, event):
        if not context.selected_objects:
            return {'CANCELLED'}
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}

        if not self.replace_from:
            return {'CANCELLED'}

        objects = bpy.context.selected_objects

        for obj in objects:
            obj.name = obj.name.replace(self.replace_from, self.replace_to)

        return {'FINISHED'}


class SUFFIXER_OT_auto(bpy.types.Operator):
    bl_idname = "suffixer.auto"
    bl_label = "auto Operator"
    bl_description = "Auto Operator"

    def execute(self, context):
        self.report({'INFO'}, "Suffix Auto")
        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected")
            return {'CANCELLED'}

        asset_type_id = context.scene.export_settings.asset_type
        config = load_config()

        for t in config.asset_types:
            if t.name_id == asset_type_id :
                self.report({'INFO'}, "ID Found")
                name_convention = t.naming_convention

                for obj in context.selected_objects:
                    obj.name = name_convention.prefix + obj.name + name_convention.suffix


        return {'FINISHED'}



CLASSES = (
    SUFFIXER_OT_prefix,
    SUFFIXER_OT_suffix,
    SUFFIXER_OT_replace,
    SUFFIXER_OT_auto,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    del bpy.types.Scene.export_settings

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
