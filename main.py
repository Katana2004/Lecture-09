# Task 1

from abc import ABC, abstractmethod
import math
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(f"Area of circle: {circle.area()}, Perimetr of circle: {circle.perimeter()}")
print(f"Area of rectangle: {rectangle.area()}, Perimeter of rectngle: {rectangle.perimeter()}")
print(f"Area of tringle: {triangle.area()}, Perimeter of triangle: {triangle.perimeter()}")

# Task 2

from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
class CreditCard(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing credit card payment of {amount} USD")
class BankTransfer(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing bank transfer of {amount} USD")
class EWallet(PaymentMethod):
    def make_payment(self, amount):
        print(f"Processing e-wallet payment of {amount} USD")
class PaymentProcessor:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def make_payment(self, amount, method_index):
        if 0 <= method_index < len(self.payment_methods):
            payment_method = self.payment_methods[method_index]
            payment_method.make_payment(amount)
        else:
            print("Invalid payment method index")

credit_card = CreditCard()
bank_transfer = BankTransfer()
e_wallet = EWallet()

payment_processor = PaymentProcessor()

payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)

payment_processor.make_payment(50, 0)
payment_processor.make_payment(100, 1)
payment_processor.make_payment(30, 2)
