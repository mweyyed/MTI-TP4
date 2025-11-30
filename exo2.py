#Adding a new payment method = modify this class → OCP violation.

from abc import ABC, abstractmethod
#Abstract Strategy
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#Concrete Strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Bitcoin")


#Payment Processor
class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def process(self, amount):
        self.method.pay(amount)



processor = PaymentProcessor(PayPalPayment())
processor.process(50)
