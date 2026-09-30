from solid.interfaces.payment_method import IPaymentMethod
from solid.interfaces.refundable import IRefundable

class WalletPayment(IPaymentMethod, IRefundable):
    @property
    def name(self) -> str:
        return "Digital Wallet"

    def process(self, amount: float) -> None:
        print(f"Deducted ${amount:.2f} from Digital Wallet balance.")

    def refund(self, amount: float) -> None:
        print(f"Re-credited ${amount:.2f} to Digital Wallet balance.")