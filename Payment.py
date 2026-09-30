class Payment:
    """
    Brute-force monolithic implementation before applying SOLID principles.
    Violations:
    - SRP: Handles payment processing, validation, and refund logic in one place.
    - OCP: Requires modifying this class every time a new payment method is added.
    - LSP / ISP: Throws runtime errors for unsupported operations (e.g., Cash refunds).
    - DIP: Directly couples callers to a concrete monolithic class.
    """

    def process_payment(self, payment_type: str, amount: float, **kwargs) -> None:
        if payment_type == "CREDIT_CARD":
            card_number = kwargs.get("card_number", "")
            cvv = kwargs.get("cvv", "")
            # Validation logic mixed with processing logic
            if len(card_number) != 16 or len(cvv) != 3:
                raise ValueError("Invalid Credit Card details.")
            print(f"Validating card ending in {card_number[-4:]}...")
            print(f"Processing Credit Card payment of ${amount:.2f}")

        elif payment_type == "UPI":
            upi_id = kwargs.get("upi_id", "")
            # Validation logic mixed with processing logic
            if "@" not in upi_id:
                raise ValueError("Invalid UPI ID.")
            print(f"Validating UPI ID: {upi_id}...")
            print(f"Processing UPI payment of ${amount:.2f}")

        elif payment_type == "CASH":
            print(f"Processing Cash on Delivery of ${amount:.2f}")

        elif payment_type == "PAYPAL":
            print(f"Authenticating with PayPal...")
            print(f"Processing PayPal payment of ${amount:.2f}")

        elif payment_type == "WALLET":
            print(f"Checking wallet balance...")
            print(f"Processing Wallet payment of ${amount:.2f}")

        else:
            raise ValueError(f"Unsupported payment type: {payment_type}")

    def refund_payment(self, payment_type: str, amount: float) -> None:
        if payment_type == "CREDIT_CARD":
            print(f"Refunding ${amount:.2f} to Credit Card.")
        elif payment_type == "UPI":
            print(f"Refunding ${amount:.2f} to UPI account.")
        elif payment_type == "PAYPAL":
            print(f"Refunding ${amount:.2f} to PayPal account.")
        elif payment_type == "WALLET":
            print(f"Refunding ${amount:.2f} to Wallet account.")
        elif payment_type == "CASH":
            # Forcing refund on a type that cannot support it
            raise RuntimeError("Cash payments cannot be refunded online.")
        else:
            raise ValueError(f"Refund not supported for payment type: {payment_type}")


# Optional test run for brute force
if __name__ == "__main__":
    payment_service = Payment()

    # Credit Card
    payment_service.process_payment("CREDIT_CARD", 150.0, card_number="4111222233334444", cvv="123")
    payment_service.refund_payment("CREDIT_CARD", 150.0)

    print("---")

    # Cash
    payment_service.process_payment("CASH", 50.0)
    try:
        payment_service.refund_payment("CASH", 50.0)
    except RuntimeError as e:
        print(f"Error: {e}")