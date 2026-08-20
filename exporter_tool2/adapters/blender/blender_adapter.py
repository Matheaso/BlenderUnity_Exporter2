import bpy

from exporter_tool2.core.types import AssetDomain
from exporter_tool2.core.adapter_interfaces.adapter_interface import AdapterInterface
from exporter_tool2.core.asset_data import AssetData, AssetPackage
from exporter_tool2.core.result import Result
from exporter_tool2.core.types import ObjectType


class BlenderAdapter(AdapterInterface):

    @staticmethod
    def create_asset_data(obj: bpy.types.Object) -> AssetData:
        return AssetData(
            obj.name,
            ObjectType(obj.type),
            []
        )

    @staticmethod
    def create_asset_package(objects: tuple[bpy.types.Object, ...]) -> AssetPackage:
        package = []
        for obj in objects:
            add = BlenderAdapter.create_asset_data(obj)
            package.append(add)

        return AssetPackage(tuple(package))

    @staticmethod
    def get_selected_assets() -> AssetPackage | None:
        package = []
        for obj in bpy.context.selected_objects:
            if not obj.type == 'MESH':
                continue
            add = BlenderAdapter.create_asset_data(obj)
            package.append(add)

        return AssetPackage(tuple(package))

    @staticmethod
    def get_selected_asset() -> Result[AssetData]:
        selection = bpy.context.active_object

        if not selection:
            return Result.error("Nothing selected")

        asset_data = BlenderAdapter.create_asset_data(selection)

        return Result.ok(asset_data)

    @staticmethod
    def get_selected_object(selection) -> bpy.types.Object | None:
        if not selection:
            return None

        return selection

    @staticmethod
    def get_export_package_from_selection(selection) -> bpy.types.Collection | None:

        if selection is None:
            return None

        for collection in selection.users_collection:
            if collection.name.startswith("EP_"):
                return collection

        return None

    @staticmethod
    def get_module_from_root(root: bpy.types.Collection, type: AssetDomain) -> bpy.types.Object | None:
        for obj in root.objects:
            if obj.name.startswith(type.value):
                return obj
        return None

    @staticmethod
    def handle_result(result: Result, reporter=None):
        reporter.report(
            {result.severity.value},
            result.message
        )

        if result.success:
            return {'FINISHED'}
        else:
            return {'CANCELLED'}

    @staticmethod
    def create_asset_package_from_selection(selection: bpy.types.Context) -> AssetPackage | None:
        if not selection:
            return None

        objects = []
        for obj in selection.selected_objects:
            data = AssetData(
                name=obj.name,
                object_type=ObjectType(obj.type),
                components=[]
            )
            objects.append(data)
        return AssetPackage(tuple(objects))

    @staticmethod
    def create_package_node():
        pass

    @staticmethod
    def get_export_objects(root: bpy.types.Collection) -> tuple[bpy.types.Object, ...]:
        objects = []

        valid_domains = {
            domain.value
            for domain in AssetDomain
        }

        for module in root.objects:
            if module.name not in valid_domains:
                continue
            objects.extend(module.children)

        return tuple(objects)
