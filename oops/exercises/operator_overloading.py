class Angle:
    def __init__(self, degree: float):
        self.degree: float = degree

    def __add__(self, other):
        res = Angle(self.degree + other.degree)
        return res

    def __str__(self):
        return str(self.degree)


a1 = Angle(40)
a2 = Angle(30)

ans = a1 + a2

print(ans)
