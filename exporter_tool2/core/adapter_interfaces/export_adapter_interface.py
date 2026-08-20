from abc import ABC, abstractmethod
from pathlib import Path

from exporter_tool2.core.serialization import load_config


class ExportAdapterInterface(ABC):

    def __init__(self, active_asset_type) -> None:
        config = load_config()

        self.filepath = (
                Path(config.project_dir)
                / active_asset_type.relative_path
        )

    @abstractmethod
    def export(
            self,
            objects,
            asset_name: str,
    ) -> None:
        pass
