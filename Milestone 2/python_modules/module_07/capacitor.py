from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creature(healing_factory: HealingCreatureFactory) -> None:
    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()

    print("Testing Creature with healing capability\n base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transforming_capability(
        transforming_factory: TransformCreatureFactory) -> None:
    base = transforming_factory.create_base()
    evolved = transforming_factory.create_evolved()
    print("Testing Creature with transform capability\n base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transforming_factory = TransformCreatureFactory()
    test_healing_creature(healing_factory)
    print()
    test_transforming_capability(transforming_factory)


if __name__ == "__main__":
    main()
