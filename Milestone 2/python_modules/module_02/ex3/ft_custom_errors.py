class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")
    else:
        print("The tomato plant is growing well")


def check_water(has_water: bool) -> None:
    if not has_water:
        raise WaterError("Not enough water in the tank!")
    else:
        print("The tomato plant has enough water in the tank")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    try:
        check_plant(True)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing WaterError...")
    try:
        check_water(False)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as e:
        print(f"Caught {GardenError.__name__}: {e}")
    try:
        check_water(False)
    except GardenError as e:
        print(f"Caught {GardenError.__name__}: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
