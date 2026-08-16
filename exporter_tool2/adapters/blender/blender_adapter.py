import bpy

from core.adapter_interface import AdapterInterface
from core.asset_data import AssetData, AssetPackage
from core.result import Result
from core.types import ObjectType


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
    def get_selected_asset() -> AssetData | None:
        active_obj = bpy.context.active_object
        if not active_obj:
            return None

        return BlenderAdapter.create_asset_data(
            active_obj
        )

    @staticmethod
    def get_export_package_name_from_selection() -> str | None:
        active_object = bpy.context.active_object

        if active_object is None:
            return None

        for collection in active_object.users_collection:
            if collection.name.startswith("EP_"):
                return collection.name
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
    def is_asset_in_export_package() -> bool:
        pass

    @staticmethod
    def create_package_node():
        pass

    @staticmethod
    def create_export_package():
        pass
