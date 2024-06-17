#allows to dynamically change the behaviour of the object by encapsulating it into various strategies
#payment service system
# we have multiple payment services that pay through some concrete strategies
# Strategy pattern involves Context class , Strategy interface,Concrete Strategies class
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):

    def pay(self):
        print("Pay through credit card succesfful.")

class DebitCardPayment(Payment):

    def pay(self):
        print("Pay through debit card succesfful.")

class UPIPayment(Payment):

    def pay(self):
        print("Pay through UPI card succesfful.")


class Orders():

    def __init__(self, payment_obj: Payment):
        self.payment_obj = payment_obj
    def pay(self):
        self.payment_obj.pay()


def main():
    credit_card = CreditCardPayment()
    debit_card = DebitCardPayment()
    upipayment = UPIPayment()
    Orders(credit_card).pay()
    Orders(debit_card).pay()
    Orders(upipayment).pay()


if __name__ == "__main__":
    main()



