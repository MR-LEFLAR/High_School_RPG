#  Name: Jaden Leflar
#  Period: 4
#  Course: CS30
#  Date created: 12/12/19
#  Description: Using th Python Standard Library

#  Imports random variable generator
from random import randint

#  Creates a place holder for the main variables
userinput = "quit"
walking_direction = "quit"
player_option = "blank"
name = ""

#  The location of the main character on the map
x = 5
y = 6

#  Total of gum
gum_total = 10

#  Inventory of the main character
Inventory = {
        "Gum": {"Total pieces left": 10},
        "Wallet": {"Total cash": "$12.27"},
        "Backpack": {"Binder": "Used to refer to notes for tests",
        "Pencil": "Used to write tests and notes, can have more than one",
        "Eraser": "Used to erase tests and notes, can have more than one",
        "Lunch": "Can be eaten at any time",
        "Map": "Can be used to see where classes are"}
            }

#  Visible representation of the map
layer1 = [' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
layer2 = [' 1 ', ' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
layer3 = [' 2 ', ' | ',' M ',' . ',' . ',' . ',' . ',' . ',' S ',' | ']
layer4 = [' 3 ', ' | ',' _ ',' _ ',' _ ',' . ',' _ ',' _ ',' _ ',' | ']
layer5 = [' 4 ', ' | ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' | ']
layer6 = [' 5 ', ' | ',' . ',' | ',' . ',' . ',' . ',' | ',' . ',' | ']
layer7 = [' 6 ', ' | ',' E ',' | ',' . ',' P ',' . ',' | ',' . ',' | ']
layer8 = [' 7 ', ' | ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' | ']

#  Inputs layers into a list
Layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8]

#  Class that organizes the students marks
class Grades:
    def __init__(self, english, math, science):
        #  English = E
        self.english = english
        #  Math = M
        self.math = math
        #  Science = S
        self.science = science
    def english_grade(self):
        print(f"Your English grade is {self.english}%")
    def math_grade(self):
        print(f"Your Math grade is {self.math}%")
    def science_grade(self):
        print(f"Your Science grade is {self.science}%")

# JADEN, Make sure you change these to variables
your_grades = Grades(0, 0, 0)
your_grades.english_grade()
your_grades.math_grade()
your_grades.science_grade()

"""Introduction"""
def the_intro(message):
    #  Principal asks for students name
    print(message)
    global name
    name = str(input()).lower()
    while name == "":
        print("You must have a name.")
        name = str(input()).lower()
    else:
        #  She repsonds
        print(f"I see...")
    print("Just one moment please.")
    #  player has to type anything to progress
    #  Makes it feel as if you are waiting and breaks up the many text boxes
    input()
    #  Shows that she is actually doing something
    print("\tShe clicks her mouse and shuffles through papers")
    input()
    input()
    print(f"Well {name.upper()},")
    #  YOU ARE IN SCHOOL NOW YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH
    print(f"I'm glad to say that you are enroled in Sheetie school!")
    i_lied_about_that_being_the_last_one = input()
    print("Here are your classes.")
    paper = input("\ttype 'paper' to view your classes ").lower()
    #  Lets the player make his first choice
    if paper == "paper":
        print(" Peroid 1 is English\n Peroid 2 is Math\n Peroid 3 is Science")
    else:
        print("Well you will have to look at it at some point")
    print(f"Do not be late please.")
    input()

the_intro("It says your name here is...")

# Imports the introduction menu with the logo and title screen
import Menu

print("""
    =====================================================================
    ------------------------------- DAY 1 -------------------------------
    =====================================================================
""")

print(f"Alright {name}, I don't know why you are here but you are...")
print(f"Anyways, Welcome to HIGH SHEETI SCHOOL!\n")
print("You want to play it?")
play_option = input("type 'yes' or 'no'").lower()
if player_option == "yes":
    print("GREAT!")
elif player_option == "no":
    print("Wow, f*** you then")
    main_character = "quit"
    userinput = "not_quit"
else:
    print(f"\t\t**Invalid input**")

#  Allows for user imput
while userinput != "quit":
    #  Shows the inventory to the player
    print("THIS IS YOUR INVENTORY")
    for item in Inventory:
        print(f"\t{item.upper()}")
    print("Type name of each item to see their values")
    print("Press 'quit' to end the game")
    userinput = input().lower()
    #  Makes it easier to read
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    if userinput == "gum":
        print(f"\tYou have {gum_total} pieces left")
        print("DO YOU WANT A PIECE?")
        print("Type 'yes' or 'no'")
        userinput = input().lower()
        #  Shows when they have no gum
        if gum_total == 0:
            print("You have no more gum, good job")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        #  Allows the user to eat the gum
        elif userinput == "yes":
            x = x - 1
            print(f"\tYou have {gum_total} pieces left")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            out_come = randint(1, 3)
            if out_come == 1:
                print("It was a bad piece and it tasted terrible")
            elif out_come == 2:
                print("Tasted pretty good, not bad")
            elif out_come == 3:
                print("You blew a bubble and it popped all over your face")
        elif userinput == "no":
            print("GOOD CHOICE")
        #  The player can quit at any time
        elif userinput == "quit":
            print("Thanks for playing")
        #  Can go back on menus
        else:
            print(f"\t\t**Invalid input**")
    elif userinput == "wallet":
        wallet = 12.27
        print(f"You have ${wallet} in your wallet")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    elif userinput == "backpack":
        #  This is inside your backpack
        print("This is inside your backpack")
        print(f"\tBINDER")
        print(f"\tMAP")
        print(f"\tLUNCH")
        userinput = input().lower()
        if userinput == "binder":
            print("just notes in here, you don't need to look at them")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        if userinput == "lunch":
            print("YOU HAVE A LUNCH")
            print("\tTurkey sandwich with mayo and lettuce")
            print("\tCut up and washed strawberries")
            print("\tA granola bar - chocolate chip kind")
            print("\tAnd a juice box of mixed berry")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        elif userinput == "map":
            #  prints map with borders
            print("<><><><><><><><><><><><><><>")
            for layer in Layers:
                print(*layer, sep='')
            print("<><><><><><><><><><><><><><>")
            #  Prints Legend
            print("\tE = English class")
            print("\tM = Math class")
            print("\tS = Science class")
            print("\tP = Entrace, Where the player starts")
            print("DO YOU WANT TO START WALKING?")
            print("\t type 'yes' or 'no'")
            userinput = input().lower()
            if userinput == "yes":
                # Tells player the comands when walking
                print("TYPE A COMMAND")
                print("\t'up' to go up")
                print("\t'down' to go down")
                print("\t'left' to go left")
                print("\t'right' to go right")
                print("\t'quit'")
                print("\t'map' to view the map again")
                userinput = "quit"
                walking_direction = input().lower()
            elif userinput == "no":
                print("WOW OK")
                print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            else:
                print(f"\t\t**Invalid input**")
        else:
            print(f"\t\t**Invalid input**")
    elif userinput == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**")

#  Part of the game where the player has to walk to class
while walking_direction != "quit" and userinput == "quit":
    #  Shows the objective
    print("!Please get to english class!")
    print("THESE ARE YOUR COORDINATES")
    print(f"\t{x}, {y}")
    walking_direction = input().lower()
    #  Allows player to move up
    if walking_direction == "up":
        y = y - 1
        if y == 1:
            y = y + 1
            print("You have ran into a wall, good job!")
        elif x == 2 and y == 6:
            print("Nice, you actually got to class, that's shocking")
            walking_direction = "quit"
        #  States the restrictions of the player for movement
        elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 3 and y == 5) or (x == 3 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 7 and y == 5) or (x == 7 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 2 and y == 2) or (x == 8 and y == 2):
            print("Wrong class dummy")
    #  Allows player to move down
    elif walking_direction == "down":
        y = y + 1
        if y == 7:
            y = y - 1
            print("You have ran into a wall, good job!")
        elif x == 2 and y == 6:
            print("Nice, you actually got to class, that's shocking")
            walking_direction = "quit"
        #  States the restrictions of the player for movement
        elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 3 and y == 5) or (x == 3 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player for movement
        elif (x == 7 and y == 5) or (x == 7 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  Shows when the player reaches the wrong classroom
        elif (x == 2 and y == 2) or (x == 8 and y == 2):
            print("Wrong class dummy")
    #  Allows player to move left
    elif walking_direction == "left":
        x = x - 1
        if x == 1:
            x = x + 1
            print("You have ran into a wall, good job!")
        elif x == 2 and y == 6:
            print("Nice, you actually got to class, that's shocking")
            walking_direction = "quit"
        #  States the restrictions of the player
        elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 3 and y == 5) or (x == 3 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 7 and y == 5) or (x == 7 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  Shows when the player reaches the wrong classroom
        elif (x == 2 and y == 2) or (x == 8 and y == 2):
            print("Wrong class dummy")
    #  Allows player to move right
    elif walking_direction == "right":
        x = x + 1
        if x == 9:
            x = x - 1
            print("You have ran into a wall, good job!")
        elif x == 2 and y == 6:
            print("Nice, you actually got to class, that's shocking")
            walking_direction = "quit"
        #  States the restrictions of the player
        elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and y == 3):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 3 and y == 5) or (x == 3 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  States the restrictions of the player
        elif (x == 7 and y == 5) or (x == 7 and y == 6):
            print("You ran into another wall, good job")
            print("Because of that, you are going back to the start")
            x = 5
            y = 6
        #  Shows when the player reaches the wrong classroom
        elif (x == 2 and y == 2) or (x == 8 and y == 2):
            print("Wrong class dummy")
    # Player can reprint map at any time
    elif walking_direction == "map":
        #  Prints map with borders
        print("<><><><><><><><><><><><><><>")
        for layer in Layers:
            print(*layer, sep='')
        print("<><><><><><><><><><><><><><>")
        #  Prints Legend
        print("\tE = English class")
        print("\tM = Math class")
        print("\tS = Science class")
        print("\tP = Entrace, Where the player starts")
    #  The player can quit at any time
    elif walking_direction == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**")
