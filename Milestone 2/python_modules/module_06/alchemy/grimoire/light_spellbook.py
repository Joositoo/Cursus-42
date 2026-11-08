from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_mname: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_mname} ({result})"
    return f"Spell rejected: {spell_mname} ({result})"
