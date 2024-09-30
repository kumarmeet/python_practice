import math
from typing import Tuple


class Polygon:
    sides: Tuple[float, ...]
    no_of_sides: int

    def __init__(self, *sides: float, no_of_sides: int):
        self.sides = tuple(sides)
        self.no_of_sides = no_of_sides


class Triangle(Polygon):

    def __init__(self, a: float, b: float, c: float):
        super().__init__(a, b, c, no_of_sides=3)

    def area(self) -> float:
        if self.no_of_sides == 3 and len(self.sides) == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2  # semi-perimeter
            return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Heron's formula
        return 0.0  # Return 0 if not a valid triangle


# Example usage
triangle = Triangle(3, 4, 5)
print(triangle.area())  # Output: 6.0
