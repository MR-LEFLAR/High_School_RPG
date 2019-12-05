# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 01/12/19
# Description: RPG Classes

"""The class of the main character description"""

# Creates a class for the main character
class main:
    # allows the player to define who their charcater is
    def __init__(self, first, last, age):
        # First name
        self.first = first
        # Last name
        self.last = last
        # Age
        self.age = age
    # Shows that the character trasnfered schools
    def school(self):
        print(f"Mr./Ms. {self.last} is now attending Scheetie School")
    # Shows the grades of the character/player
    def grades(self, math, science, english):
        # Math grade
        self.math = math_grade
        # Science grade
        self.science = science_grade
        # English grade
        self.english = english_grade
        print(f"Mr./Ms. grades are {self.math}, {self.science},")
        print(f"{self.english}, they could be better")

my_character = main("Jaden", "Leflar", 16)
print(my_character.first, my_character.last, my_character.age)

# Division line for a better look
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

# Visible representation of the map
layer1 = [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
layer2 = [' 1 ', ' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
layer3 = [' 2 ', ' | ',' M ',' . ',' . ',' . ',' . ',' . ',' S ',' | ']
layer4 = [' 3 ', ' | ',' _ ',' _ ',' _ ',' . ',' _ ',' _ ',' _ ',' | ']
layer5 = [' 4 ', ' | ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' | ']
layer6 = [' 5 ', ' | ',' . ',' | ',' . ',' . ',' . ',' | ',' . ',' | ']
layer7 = [' 6 ', ' | ',' E ',' | ',' . ',' . ',' . ',' | ',' . ',' | ']
layer8 = [' 7 ', ' | ',' _ ',' _ ',' _ ',' P ',' _ ',' _ ',' _ ',' | ']

# Inputs layers into a list
Layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8]

# Creates a class for the map
class map:
    def __init__(self, p, m, e, s):
        # Player icon on the map
        self.p = p
        # Math icon on the map
        self.m = m
        # English icon on the map
        self.e = e
        # Science icon on the map
        self.s = s

my_map = map("The Player", "Math class", "English class", "Science class")
print(f"\t{my_map.m} is 5 spaces up and 3 spaces left")
print(f"\t{my_map.e} is 3 spaces up, 3 spaces left, and 2 spaces down")
print(f"\t{my_map.s} is 5 spaces up and 3 spaces right")
