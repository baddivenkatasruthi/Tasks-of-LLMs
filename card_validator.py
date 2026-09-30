from solid.interfaces.validator import IPaymentValidator

class CreditCardValidator(IPaymentValidator):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv

    def validate(self) -> bool:
        print(f"Validating card ending in {self.card_number[-4:]}...")
        return len(self.card_number) == 16 and len(self.cvv) == 3