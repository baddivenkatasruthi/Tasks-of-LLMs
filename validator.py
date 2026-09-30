from abc import ABC, abstractmethod

class IPaymentValidator(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass