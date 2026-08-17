from abc import ABC, abstractmethod

from exporter_tool2.core.types import PackageObjectType
from exporter_tool2.core.result import Result
from exporter_tool2.core.asset_data import AssetPackage, AssetData
from typing import TypeVar

T = TypeVar("T")

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
    def get_selected_asset() -> Result[T]:
        pass

    @staticmethod
    @abstractmethod
    def get_selected_object(selection):
        pass

    @staticmethod
    @abstractmethod
    def get_export_package_from_selection(selection) -> Result[T]:
        pass

    @staticmethod
    @abstractmethod
    def get_module_from_root(root, type: PackageObjectType) -> str | None:
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

    @staticmethod
    @abstractmethod
    def find_module():
        pass

