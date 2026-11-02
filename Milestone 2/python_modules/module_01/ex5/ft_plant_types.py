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

    def set_age(self, age: int) -> None:
        if age < 0:
            print(
                f"{self.get_name()}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self._plant_age = age

    def show(self) -> None:
        print(
            f"{self.get_name()}: "
            f"{round(self.get_height(), 2)}cm, {self.get_age()} days old"
        )

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8 * self.get_growth_rate())

    def age(self) -> None:
        self.set_age(self.get_age() + 1)


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                plant_age: int,
                growth_rate: float,
                colour: str) -> None:
        self._colour = colour
        self._bloomed = False
        super().__init__(name, height, plant_age, growth_rate)

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._colour}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: float,
                plant_age: int,
                growth_rate: float,
                trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter
        super().__init__(name, height, plant_age, growth_rate)

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self.get_height()}cm "
            f"long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
                    self,
                    name: str,
                    height: float,
                    plant_age: int,
                    growth_rate: float,
                    harvest_season: str,) -> None:
        self._has_grown = False
        self._harvest_season = harvest_season
        self._nutritional_value = 0.0
        super().__init__(name, height, plant_age, growth_rate)

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def let_grow(self, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        self._has_grown = True
        for _ in range(days):
            self.age()
            self.grow()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        if self._has_grown:
            print(f"Nutritional value: {self._nutritional_value}")
        else:
            print("Nutritional value: 0")


def main() -> None:
    chrysanthemum = Flower("Chrysanthemum", 15.0, 10, 1, "Yellow")
    oak = Tree("Oak", 100.0, 5, 0.5, 50.0)
    lettuce = Vegetable("Lettuce", 5.0, 2, 0.2, "Spring")

    print("=== Garden Plant Types ===\n=== Flower")
    chrysanthemum.show()
    chrysanthemum.bloom()
    chrysanthemum.show()
    print()
    print("=== Tree")
    oak.show()
    oak.produce_shade()
    print()
    print("=== Vegetable")
    lettuce.show()
    lettuce.let_grow(20)
    lettuce.show()


if __name__ == "__main__":
    main()
