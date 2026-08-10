from abc import ABC, abstractmethod

from ..core.asset_type_data import AssetTypeData
from ..core.object_data import ExportContext


class IRule(ABC):
    @abstractmethod
    def validate(
            self,
            export_context: ExportContext,
            asset_type_data: AssetTypeData,
    ):
        pass
