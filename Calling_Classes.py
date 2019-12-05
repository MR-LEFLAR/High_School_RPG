# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 01/12/19
# Description: RPG Classes

"""Calling the given classes"""

from CLASSES import main, map

class MyCharacter(main):1
    # Creating a child class from the main character class
    def __init__(self, first, last, age, grade):
        # recalling the __init__ function from parent class
        super().__init__(first, last, age)
        self.grade = grade

MyCharacter(Jaden, Leflar, 16, 12)
print(f"Hello {self.first} {self.last}, I see that you are {self.age} and")
print(f"are in grade {self.grade}")

my_map = map("The Player", "Math class", "English class", "Science class")
print(f"{my_map.m} is 5 spaces up and 3 spaces left")
print(f"{my_map.e} is 3 spaces up, 3 spaces left, and 2 spaces down")
print(f"{my_map.s} is 5 spaces up and 3 spaces right")
