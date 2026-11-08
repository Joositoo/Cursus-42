import abc


class Creature(abc.ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abc.abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"
