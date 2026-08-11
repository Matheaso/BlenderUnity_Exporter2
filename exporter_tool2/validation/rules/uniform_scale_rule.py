from ...core.config_data import AssetTypeData
from ...core.object_data import ExportContext
from ...validation.rule_interface import IValidationRule

class UniformScale(IValidationRule):
    rule_id = "uniform_scale"
    display_name = "Uniform Scale"
    description = ("Rule:\n"
                   "- Scale needs to be freezed)\n"
                   )

    def validate(self, export_context: ExportContext, asset_type_data: AssetTypeData):
        pass