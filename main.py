from solid.services.processor import PaymentProcessor
from solid.methods.credit_card import CreditCardPayment
from solid.methods.cash import CashPayment
from solid.methods.paypal import PayPalPayment
from solid.validators.card_validator import CreditCardValidator

if __name__ == "__main__":
    processor = PaymentProcessor()

    # 1. Credit Card with Injected Validator
    card_validator = CreditCardValidator("4111222233334444", "123")
    credit_card = CreditCardPayment(validator=card_validator)
    processor.execute_payment(credit_card, 150.0)
    processor.execute_refund(credit_card, 150.0)

    print("---")

    # 2. Cash on Delivery (Non-refundable)
    cash = CashPayment()
    processor.execute_payment(cash, 50.0)
    processor.execute_refund(cash, 50.0)

    print("---")

    # 3. PayPal Payment
    paypal = PayPalPayment()
    processor.execute_payment(paypal, 80.0)
    processor.execute_refund(paypal, 80.0)