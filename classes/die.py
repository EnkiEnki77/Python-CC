"""A class that represents a die of a certain amount of sides"""
from random import randint

class Die:
    """"A simple attempt to represent a die"""

    def __init__(self, sides = 6) -> None:
        """Initializes the attributes of a die"""
        self.sides = sides

    def roll_die(self):
        """Rolls die, and gives the number it landed on"""
        print(f"You rolled the {self.sides}-sided die and it landed on: {randint(1, self.sides)}")

    
six_sided_die = Die()

six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()
six_sided_die.roll_die()

ten_sided_die = Die(10)

ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()
ten_sided_die.roll_die()

twenty_sided_die = Die(20)

twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()
twenty_sided_die.roll_die()