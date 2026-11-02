class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(
                f"{self.name}: "
                f"{round(self.height, 2)}cm, {self.plant_age} days old"
            )

    def grow(self) -> None:
        self.height = self.height + 0.8 * self.growth_rate

    def age(self) -> None:
        self.plant_age += 1


def main() -> None:
    tulip = Plant("Tulip", 15.0, 20, 1.5)
    chrysanthemum = Plant("Chrysanthemum", 25.0, 102, 1)
    rose = Plant("Rose", 30.0, 60, 0.9)
    sunflower = Plant("Sunflower", 40.0, 15, 2.2)
    cactus = Plant("Cactus", 10.0, 365, 0.2)
    plants: list[Plant] = [tulip, chrysanthemum, rose, sunflower, cactus]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
