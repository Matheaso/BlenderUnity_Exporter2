from core.asset_type_data import AssetTypeData
from core.object_data import ExportContext
from validation.rule_interface import IRule

class naming_rule(IRule):

    def validate(self, export_context: ExportContext, asset_type_data: AssetTypeData):
        pass