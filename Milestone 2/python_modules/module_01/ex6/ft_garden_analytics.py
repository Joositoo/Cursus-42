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
        self._statistics = Plant.Statistics()

    class Statistics:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def add_count(self, action: str) -> None:
            if action == "grow":
                self._grow_count += 1
            elif action == "age":
                self._age_count += 1
            else:
                self._show_count += 1

        def display(self, name: str) -> None:
            print(
                f"[statistics for {name}]\n"
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

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
        self._statistics.add_count("show")

    def show_statistics(self) -> None:
        self._statistics.display(self._name)

    def grow(self) -> None:
        self.set_height(self.get_height() + 0.8 * self.get_growth_rate())
        self._statistics.add_count("grow")

    def age(self) -> None:
        self.set_age(self.get_age() + 1)
        self._statistics.add_count("age")

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.1)

    @staticmethod
    def older_than_a_year(days: int) -> None:
        if days <= 365:
            print(f"Is {days} days more than a year? -> False")
        else:
            print(f"Is {days} days more than a year? -> True")


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
        print(f"[asking the {self._name} to grow and bloom]")
        self._bloomed = True
        self.grow()

    def show(self) -> None:
        super().show()
        print(f"Color: {self._colour}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
                self,
                name: str,
                height: float,
                plant_age: int,
                growth_rate: float,
                colour: str) -> None:
        self._number_of_seeds = 0
        super().__init__(name, height, plant_age, growth_rate, colour)

    def bloom(self) -> None:
        print(f"[make {self._name} grow, age and bloom]")
        self._bloomed = True
        self.grow()
        self.age()
        self._number_of_seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._number_of_seeds}")


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
        self._statistics = Tree.TreeStatistics()

    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def add_count(self, action: str) -> None:
            if action == "shade":
                self._shade_count += 1
            else:
                super().add_count(action)

        def display(self, name: str) -> None:
            super().display(name)
            print(f"{self._shade_count} shade")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self.get_height()}cm "
            f"long and {self._trunk_diameter}cm wide."
        )
        self._statistics.add_count("shade")

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
                    harvest_season: str) -> None:
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


def show_info(plant: Plant) -> None:
    plant.show_statistics()


def main() -> None:
    rose = Flower("Rose", 15.0, 10, 0.2, "Red")
    tree = Tree("Oak", 200.0, 365, 0.4, 5.0)
    seed = Seed("Sunflower", 80.0, 45, 0.5, "Yellow")
    unknown_plant = Plant.unknown_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.older_than_a_year(30)
    Plant.older_than_a_year(400)

    print("\n=== Flower")
    rose.show()
    rose.show_statistics()
    rose.bloom()
    rose.show()
    show_info(rose)

    print("\n=== Tree")
    tree.show()
    tree.show_statistics()
    tree.produce_shade()
    show_info(tree)

    print("\n=== Seed")
    seed.show()
    seed.bloom()
    seed.show()
    show_info(seed)

    print("\n=== Anonymous")
    unknown_plant.show()
    show_info(unknown_plant)


if __name__ == "__main__":
    main()
