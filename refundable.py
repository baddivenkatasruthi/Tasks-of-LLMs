from abc import ABC, abstractmethod

# ISP: Separated interface for refund support
class IRefundable(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass