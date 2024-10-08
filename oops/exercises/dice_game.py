from random import randint


class Dice:
    def __init__(self, side_one: int, side_two: int):
        self.dice_one = side_one
        self.dice_two = side_two

    def roll_dice(self):
        self.dice_one = randint(1, self.dice_one)
        self.dice_two = randint(1, self.dice_two)

    def reset_dice(self):
        self.dice_one = 6
        self.dice_two = 6

    def sides(self):
        print(f"Dice one -> {self.dice_one}\n"
              f"Dice two -> {self.dice_two}")


d = Dice(6, 6)

d.roll_dice()

d.sides()
