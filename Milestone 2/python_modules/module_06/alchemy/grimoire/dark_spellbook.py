from .dark_validator import validate_dark_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_mname: str, ingredients: str) -> str:
    result = validate_dark_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_mname} ({result})"
    return f"Spell rejected: {spell_mname} ({result})"
