import math


class Circle:
    PI = math.pi

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def area(self) -> float:
        return float("{:.2f}".format(self.radius * self.radius * Circle.PI))

    def perimeter(self) -> float:
        return float("{:.2f}".format(2 * Circle.PI * self.radius))


cr = Circle(4.3)

print(cr.area())
print(cr.perimeter())
