## user defined exceptions
class NegativeAgeException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def stag(_age):
    if _age < 0:
        raise NegativeAgeException("Negative age exception")
    elif 0 < _age < 13:
        print("Kid")
    elif 13 < _age <= 19:
        print("Teen")
    elif 19 < _age <= 50:
        print("Young")
    else:
        print("Old")


try:
    age = int(input("Input age -> "))
    stag(age)
except NegativeAgeException as e:
    print(e)
