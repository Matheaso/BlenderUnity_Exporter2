from ...core.config_data import AssetTypeData
from ...core.object_data import ExportContext
from ...validation.rule_interface import IValidatonRule

class NameRule(IValidatonRule):

    def validate(self, export_context: ExportContext, asset_type_data: AssetTypeData):
        pass