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
    chrysanthemum = Plant("Chrysanthemum", 25.0, 102, 1)
    start_growth = chrysanthemum.height

    print("=== Garden Plant Growth ===\n")
    chrysanthemum.show()

    for i in range(7):
        chrysanthemum.grow()
        chrysanthemum.age()

        print(f"=== Day {i + 1} ===")
        chrysanthemum.show()

    print(
        f"Growth this week: "
        f"{round(chrysanthemum.height - start_growth, 2)}cm"
    )


if __name__ == "__main__":
    main()
