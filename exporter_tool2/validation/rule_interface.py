from abc import ABC, abstractmethod

from ..core.config_data import AssetTypeData
from ..core.object_data import ExportContext


class IValidatonRule(ABC):
    @abstractmethod
    def validate(
            self,
            export_context: ExportContext,
            asset_type_data: AssetTypeData,
    ):
        pass
