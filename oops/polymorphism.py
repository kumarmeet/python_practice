## duck typing
from abc import ABC, abstractmethod


class Creta:
    def drive(self):
        print("Driving a Creta")


class Mercedes:
    def drive(self):
        print("Driving a Mercedes")


def driver(car: Creta | Mercedes):
    ## if its acts like a talking and walking then it is a duck
    car.drive()


driver(Creta())
driver(Mercedes())


## method overloading

class Arith:
    def adding(self, *, r=0, b=0, c=0):
        return r + b + c


a = Arith()

print(a.adding(r=10, b=20))
print(a.adding(r=10, b=20, c=30))


## method overriding
class Iphone6():
    def home(self):
        print("Home button press")


class Iphone10(Iphone6):
    def home(self):
        print("Home button touch")
        super().home()


iphone = Iphone6()

iphone.home()

iphone = Iphone10()

iphone.home()


## operator overloading
class Rational:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, other):
        s = Rational(self.p, self.q)
        s.p = self.p * other.q + self.q * other.p
        s.q = self.q * other.q

        return s

    def __str__(self):
        return str(self.p) + "/" + str(self.q)


r1 = Rational(2, 3)
r2 = Rational(2, 5)

res = r1 + r2

print(res.p, res.q, res)


## abstract class and interfaces

class Parent(ABC):
    """if class has only abstract method then it will becomes interface"""

    @abstractmethod
    def show(self):
        pass


class ParentTwo(ABC):
    """if class has abstract method as well as concrete methods then it will becomes abstract class"""

    @abstractmethod
    def show_one(self):
        pass

    def display(self):
        print("Parent class two")


class Child(Parent, ParentTwo):
    def show(self):
        print("Interface")

    def show_one(self):
        print("Abstract class")


ch = Child()
ch.show()
ch.show_one()
ch.display()
