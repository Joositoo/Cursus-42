from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.heal_capability import HealCapability
from .invalid_strategy import InvalidStrategy


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if isinstance(creature, HealCapability):
            print(creature.attack())
            print(creature.heal())
        else:
            raise InvalidStrategy(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False
