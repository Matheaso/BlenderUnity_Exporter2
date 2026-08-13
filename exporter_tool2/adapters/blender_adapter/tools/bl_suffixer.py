import bpy

from ..logging.bl_result import handle_result
from ....core.object_data import create_export_context
from ....core.tools.suffixer import Suffixer


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
        self.report({'INFO'}, "Suffix Suffix")

        export_context = create_export_context(context)
        output = Suffixer.run_suffix(export_context, self.suffix)

        if not output.success:
            return handle_result(self, output)

        for operation in output.data or []:
            obj = bpy.data.objects.get(operation.old_name)

            if obj:
                obj.name = operation.new_name

        return handle_result(self, output)


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
        self.report({'INFO'}, "Suffix Prefix")

        export_context = create_export_context(context)
        output = Suffixer.run_prefix(export_context, self.prefix)

        if not output.success:
            return handle_result(self, output)

        for operation in output.data or []:
            obj = bpy.data.objects.get(operation.old_name)
            if obj:
                obj.name = operation.new_name

        return handle_result(self, output)


class SUFFIXER_OT_replace(bpy.types.Operator):
    bl_idname = "suffixer.replace"
    bl_label = "replace Operator"
    bl_description = "Replace Operator"

    old: bpy.props.StringProperty(
        name="Replace from",
        default="",
    )

    new: bpy.props.StringProperty(
        name="Replace to",
        default="",
    )

    def invoke(self, context, event):
        if not context.selected_objects:
            return {'CANCELLED'}
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        self.report({'INFO'}, "Suffix Replace")

        export_context = create_export_context(context)
        output = Suffixer.run_replace(export_context, self.old, self.new)

        if not output.success:
            return handle_result(self, output)

        for operation in output.data or []:
            obj = bpy.data.objects.get(operation.old_name)
            if obj:
                obj.name = operation.new_name

        return handle_result(self, output)


class SUFFIXER_OT_auto(bpy.types.Operator):
    bl_idname = "suffixer.auto"
    bl_label = "auto Operator"
    bl_description = "Auto Operator"

    def execute(self, context):
        self.report({'INFO'}, "Suffix Auto")

        export_context = create_export_context(context)
        asset_type = context.scene.export_settings.asset_type

        output = Suffixer.run_auto(export_context, asset_type)
        if not output.success:
            return handle_result(self, output)

        for operation in output.data or []:
            obj = bpy.data.objects.get(operation.old_name)
            if obj:
                obj.name = operation.new_name

        return handle_result(self, output)


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

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
