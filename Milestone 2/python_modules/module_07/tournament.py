from ex0 import CreatureFactory, AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    DefensiveStrategy,
    NormalStrategy,
    BattleStrategy,
    InvalidStrategy
)


def battle(opp: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opp)} opponents involved\n")

    try:
        for i in range(len(opp)):
            factory_a, strategy_a = opp[i]
            for j in range(i + 1, len(opp)):
                factory_b, strategy_b = opp[j]

                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()

                print("* Battle *")
                print(creature_a.describe())
                print(" vs.")
                print(creature_b.describe())
                print(" now fight!")

                strategy_a.act(creature_a)
                strategy_b.act(creature_b)

    except InvalidStrategy as e:
        print(e)


def main() -> None:
    aqua_factory = AquaFactory()
    flame_factory = FlameFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    normal_strategy = NormalStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
    ])

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ])


if __name__ == "__main__":
    main()
