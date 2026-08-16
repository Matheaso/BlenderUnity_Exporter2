from abc import ABC, abstractmethod

from exporter_tool2.core.result import Result
from exporter_tool2.core.asset_data import AssetPackage, AssetData


class AdapterInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_asset_data(obj) -> AssetData:
        pass

    @staticmethod
    @abstractmethod
    def create_asset_package(objects) -> AssetPackage:
        pass

    @staticmethod
    @abstractmethod
    def get_selected_assets() -> AssetPackage | None:
        pass

    @staticmethod
    @abstractmethod
    def get_selected_asset() -> AssetData | None:
        pass

    @staticmethod
    @abstractmethod
    def get_export_package_name_from_selection() -> str | None:
        pass

    @staticmethod
    @abstractmethod
    def handle_result(result: Result, reporter = None ):
        pass

    @staticmethod
    @abstractmethod
    def is_asset_in_export_package() -> bool:
        pass

    @staticmethod
    @abstractmethod
    def create_package_node():
        pass

    @staticmethod
    @abstractmethod
    def create_export_package():
        pass


