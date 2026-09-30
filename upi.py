from typing import Optional
from solid.interfaces.payment_method import IPaymentMethod
from solid.interfaces.refundable import IRefundable
from solid.interfaces.validator import IPaymentValidator

class UPIPayment(IPaymentMethod, IRefundable):
    def __init__(self, validator: Optional[IPaymentValidator] = None):
        self.validator = validator

    @property
    def name(self) -> str:
        return "UPI"

    def process(self, amount: float) -> None:
        if self.validator and not self.validator.validate():
            raise ValueError("UPI validation failed.")
        print(f"Transferred ${amount:.2f} via UPI.")

    def refund(self, amount: float) -> None:
        print(f"Refunded ${amount:.2f} to UPI ID.")