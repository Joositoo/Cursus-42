import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name, quantity = arg.split(":", 1)
        item_name = item_name.strip()
        quantity = quantity.strip()

        if item_name == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
            else:
                inventory.update({item_name: int(quantity)})
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    return inventory


def show_info(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(
        f"Total quantity of the {len(inventory)} "
        f"items: {sum(inventory.values())}"
    )

    for item in inventory:
        print(
            f"Item {item} represents "
            f"{round(inventory[item] / sum(inventory.values()) * 100, 1)}%"
        )

    for item in inventory:
        quantity_most_abundant = inventory[item]
        name_most_abundant = item
        break

    for item in inventory:
        if inventory[item] > quantity_most_abundant:
            quantity_most_abundant = inventory[item]
            name_most_abundant = item
    print(
        f"Item most abundant: {name_most_abundant} "
        f"with quantity {quantity_most_abundant}"
    )

    quantity_least_abundant = quantity_most_abundant
    name_least_abundant = name_most_abundant
    for item in inventory:
        if inventory[item] < quantity_least_abundant:
            name_least_abundant = item
            quantity_least_abundant = inventory[item]
    print(
        f"Item least abundant: {name_least_abundant} "
        f"with quantity {quantity_least_abundant}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def inventory_system() -> None:
    if len(sys.argv) < 2:
        print(
            "No items provided. Usage: python3 "
            "ft_inventory_system.py <item1>:<quantity1> "
            "<item2>:<quantity2> ..."
        )
        return

    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()
    if len(inventory) == 0:
        print("No valid items were provided.")
        return

    show_info(inventory)


if __name__ == "__main__":
    inventory_system()
