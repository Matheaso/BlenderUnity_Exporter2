from .rules.naming_rule import NameRule
from .rules.uniform_scale_rule import UniformScale

RULE_REGISTRY = {
    NameRule.rule_id: NameRule,
    UniformScale.rule_id: UniformScale,
}

def get_rule_class(rule_id: str):
    return RULE_REGISTRY.get(rule_id)

def get_rule_items() -> tuple[tuple[str, str, str], ...]:
    return tuple(
        (
            rule_id,
            rule_class.display_name,
            rule_class.description,
        )
        for rule_id, rule_class in RULE_REGISTRY.items()
    )