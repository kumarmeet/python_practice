class Calc:
    def __init__(self):
        pass

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


x, y = 10, 20

print(Calc.addition(x, y))
print(Calc.subtraction(x, y))
print(Calc.multiplication(x, y))
print(Calc.division(x, y))
