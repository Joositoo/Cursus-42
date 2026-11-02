class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            growth_rate: float) -> None:
        self._name = name
        if height < 0:
            print(
                f"{self._name}: Error, height can't be negative, "
                "using default value 0.0"
                )
            self._height = 0.0
        else:
            self._height = height
        if plant_age < 0:
            print(
                f"{self._name}: Error, age can't be negative, "
                "using default value 0"
            )
            self._plant_age = 0
        else:
            self._plant_age = plant_age
        if growth_rate < 0:
            print(
                f"{self._name}: "
                "Error, growth rate can't be negative, using default value 0.1"
            )
            self._growth_rate = 0.1
        else:
            self._growth_rate = growth_rate
        print("Plant created:", end=" ")
        self.show()

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._plant_age

    def get_growth_rate(self) -> float:
        return self._growth_rate

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self.get_name()}: Error, height can't be negative\n"
                "Height update rejected"
            )
        else:
            self._height = height
            print(f"Height updated: {round(self._height, 2)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(
                f"{self.get_name()}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self._plant_age = age
            print(f"Age updated: {self._plant_age} days")

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{round(self.get_height(), 2)}cm, {self.get_age()} days old"
        )

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8 * self.get_growth_rate())

    def age(self) -> None:
        self.set_age(self.get_age() + 1)


def main() -> None:
    print("=== Garden Security System ===")
    chrysanthemum = Plant("Chrysanthemum", 15.0, 10, 1)
    print()
    chrysanthemum.set_height(25)
    chrysanthemum.set_age(30)
    print()
    chrysanthemum.set_height(-40)
    chrysanthemum.set_age(-110)
    print()
    print("Current state:", end=" ")
    chrysanthemum.show()


if __name__ == "__main__":
    main()
