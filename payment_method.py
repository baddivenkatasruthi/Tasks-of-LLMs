from abc import ABC, abstractmethod

class IPaymentMethod(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def process(self, amount: float) -> None:
        pass