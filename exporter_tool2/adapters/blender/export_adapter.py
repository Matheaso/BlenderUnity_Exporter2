import bpy
from exporter_tool2.core.adapter_interfaces.export_adapter_interface import ExportAdapterInterface


class BlenderExportAdapter(ExportAdapterInterface):

    def export(
            self,
            objects: tuple[bpy.types.Object, ...],
            asset_name: str,
    ) -> None:

        filepath = self.filepath / f"{asset_name}.fbx"

        if not objects:
            return

        bpy.ops.object.select_all(action='DESELECT')

        for obj in objects:
            obj.select_set(True)

        bpy.context.view_layer.objects.active = objects[0]

        bpy.ops.export_scene.fbx(
            filepath=str(filepath),
            use_selection=True,
            apply_unit_scale=True,
            apply_scale_options="FBX_SCALE_ALL",
            axis_forward="-Z",
            axis_up="Y",
            add_leaf_bones=False,
            bake_anim=False,
            use_space_transform=True,
            bake_space_transform=True,
        )
