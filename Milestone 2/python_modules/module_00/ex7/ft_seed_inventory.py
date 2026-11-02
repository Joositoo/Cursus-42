def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    message = f"{seed_type.capitalize()} seeds: "
    match unit:
        case "packets":
            message += f"{quantity} packets available"
        case "grams":
            message += f"{quantity} grams total"
        case "area":
            message += f"covers {quantity} square meters"
        case _:
            message = "Unknown unit type"
    print(message)
