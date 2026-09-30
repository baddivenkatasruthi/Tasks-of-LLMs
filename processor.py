from solid.interfaces.payment_method import IPaymentMethod
from solid.interfaces.refundable import IRefundable

class PaymentProcessor:
    # DIP: High-level module depends on abstraction (IPaymentMethod)
    def execute_payment(self, payment_method: IPaymentMethod, amount: float) -> None:
        print(f"Initiating checkout with {payment_method.name}...")
        payment_method.process(amount)

    def execute_refund(self, payment_method: IPaymentMethod, amount: float) -> None:
        if isinstance(payment_method, IRefundable):
            payment_method.refund(amount)
        else:
            print(f"Refund Error: {payment_method.name} does not support online refunds.")