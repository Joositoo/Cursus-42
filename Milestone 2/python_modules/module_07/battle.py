from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factories(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        flameling_factory: CreatureFactory,
        aqua_factory: CreatureFactory
        ) -> None:
    fighter_a = flameling_factory.create_base()
    fighter_b = aqua_factory.create_base()

    print("Testing battle")
    print(f"{fighter_a.describe()} \n vs\n{fighter_b.describe()}")
    print(f" fight!\n{fighter_a.attack()}\n{fighter_b.attack()}")


def main() -> None:
    flameling_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factories(flameling_factory)
    print()
    test_factories(aqua_factory)
    print()
    test_battle(flameling_factory, aqua_factory)


if __name__ == "__main__":
    main()
