from solid.interfaces.validator import IPaymentValidator

class UPIValidator(IPaymentValidator):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def validate(self) -> bool:
        print(f"Validating UPI ID: {self.upi_id}...")
        return "@" in self.upi_id