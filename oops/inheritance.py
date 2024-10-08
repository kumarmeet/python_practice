class Rectangle:
    length: float
    breadth: float

    def __init__(self, *, l: float = 0.0, b: float = 0.0):
        self.length = l
        self.breadth = b

    ## mutators
    def set_length(self, l: float) -> None:
        self.length = l

    def set_breadth(self, b: float) -> None:
        self.breadth = b

    ## accessors
    def get_length(self) -> float:
        return self.length

    def get_breadth(self) -> float:
        return self.breadth

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)


class Cube(Rectangle):
    """
    there are two options to call parent constructor
        1. super().__init__(l=l, b=b)
        2. self.length = l, self.breadth = b

        Note: Whenever you write a child class constructor for child class
              the parent class constructor will be hidden (shadowed).
              You have to call explicitly (manually)
    """

    height: float

    def __init__(self, l: float, b: float, h: float):
        super().__init__(l=l, b=b)
        self.height = h

    def set_height(self, h: float) -> None:
        self.height = h

    def get_height(self) -> float:
        return self.height

    def total_area(self) -> float:
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def lid_area(self) -> float:
        return self.length * self.breadth

    def volume(self) -> float:
        return self.length * self.breadth * self.height


## client code

rec1 = Rectangle(l=10, b=20)

print(rec1.area())

c1 = Cube(l=rec1.get_length(), b=rec1.get_breadth(), h=30)

print(c1.volume())
