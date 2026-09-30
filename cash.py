from solid.interfaces.payment_method import IPaymentMethod

# Cash does NOT inherit from IRefundable (ISP & LSP)
class CashPayment(IPaymentMethod):
    @property
    def name(self) -> str:
        return "Cash on Delivery"

    def process(self, amount: float) -> None:
        print(f"Order placed for Cash on Delivery: ${amount:.2f}.")