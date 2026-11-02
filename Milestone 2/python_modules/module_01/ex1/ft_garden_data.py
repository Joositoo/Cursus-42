class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    chrysanthemum = Plant("Chrysanthemum", 45, 102)
    tulip = Plant("Tulip", 30, 142)
    sunflower = Plant("Sunflower", 77, 150)

    print("=== Garden Plant Registry ===")
    chrysanthemum.show()
    tulip.show()
    sunflower.show()


if __name__ == "__main__":
    main()
