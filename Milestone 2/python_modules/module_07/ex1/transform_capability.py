import abc


class TransformCapability(abc.ABC):

    @abc.abstractmethod
    def transform(self) -> str:
        ...

    @abc.abstractmethod
    def revert(self) -> str:
        ...
