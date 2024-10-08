class Cuboid:
    """in python constructor cannot be overloaded"""

    ## use __ make private instance variable

    __count = 0  ## static property
    __length: float
    __breadth: float
    __height: float

    def __init__(self, *, l=0, b=0, h=0):
        self.__length = l
        self.__breadth = b
        self.__height = h
        Cuboid.__count += 1

    ## mutators
    def set_length(self, l):
        self.__length = l

    def set_breadth(self, b):
        self.__breadth = b

    def set_height(self, h):
        self.__height = h

    ## accessors
    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    def get_height(self):
        return self.__height

    @classmethod
    def class_method(cls):
        # Cuboid.count = 3
        return cls.__count

    ## static method in python they don't access any member of a class
    @staticmethod
    def static_method(length, breadth):
        return length == breadth

    def total_area(self):
        return 2 * (self.__length * self.__breadth + self.__breadth * self.__height + self.__length * self.__height)

    def lid_area(self):
        return self.__length * self.__breadth

    def volume(self):
        return self.__length * self.__breadth * self.__height


## client code
c1 = Cuboid(l=10, b=20, h=30)

print(c1.volume(), c1.total_area(), c1.lid_area())

print(dir(Cuboid))
print(tuple(vars(c1).keys()), type(c1))

c2 = Cuboid(l=20, b=20)

print(id(c2))

print(Cuboid.class_method())

print(Cuboid.static_method(10, 10))
