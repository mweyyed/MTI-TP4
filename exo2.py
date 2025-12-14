from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
       

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        

class BitcoinPayment(PaymentMethod):
    def pay(self, amount):
        


