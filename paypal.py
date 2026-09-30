from solid.interfaces.payment_method import IPaymentMethod
from solid.interfaces.refundable import IRefundable

class PayPalPayment(IPaymentMethod, IRefundable):
    @property
    def name(self) -> str:
        return "PayPal"

    def process(self, amount: float) -> None:
        print(f"Authenticated with PayPal and charged ${amount:.2f}.")

    def refund(self, amount: float) -> None:
        print(f"Refunded ${amount:.2f} to PayPal account.")