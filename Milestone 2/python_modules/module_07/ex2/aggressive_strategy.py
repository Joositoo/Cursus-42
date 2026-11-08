from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.transform_capability import TransformCapability
from .invalid_strategy import InvalidStrategy


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidStrategy(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False
