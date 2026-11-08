from .battle_strategy import BattleStrategy
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True
