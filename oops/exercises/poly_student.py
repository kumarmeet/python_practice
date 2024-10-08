class Cat:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def info(self):
        print(self.name, self.age, "CAT")

    def make_sound(self):
        print("Mewo", self.name)


class Dog:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def info(self):
        print(self.name, self.age, "CAT")

    def make_sound(self):
        print("Bark", self.name)


## duck typing approach
def my_pet(pet: Cat | Dog):
    pet.info()
    pet.make_sound()


cat = Cat("Billi", 1)
dog = Dog("Kutta", 4)

my_pet(cat)
my_pet(dog)
