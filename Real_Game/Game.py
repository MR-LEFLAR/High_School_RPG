#  Name: Jaden Leflar
#  Period: 4
#  Course: CS30
#  Date created: 12/12/19
#  Description: Final project

#  Imports random variable generator
from random import randint

#  Creates a place holder for the main variables
userinput = "quit"
walking_direction = "quit"
player_option = "blank"
wallet = 12.27
name = ""
variable_name = "no"
English_class = "quit"
other_variable_name = "quit"
other_userinput = "quit"

#  Makes the variables blank, waiting for the player to input something
Enotes_1 = ""
Enotes_2 = ""
Enotes_3 = ""
Mnotes_1 = ""
Mnotes_2 = ""
Mnotes_3 = ""
Snotes_1 = ""
Snotes_2 = ""
Snotes_3 = ""


#  Your binder with all your notes and subjects
binder = {"English": {Enotes_1, Enotes_2, Enotes_3},
          "Math": {Mnotes_1, Mnotes_2, Mnotes_3},
          "Science": {Snotes_1, Snotes_2, Snotes_3}}

#  The location of the main character on the map
global x
x = 5
global y
y = 6

#  Total of gum
gum_total = 10

#  Creates the Inventory out of a nested list that will be used in game
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

#  Class that organizes the players marks
class Grades:
    def __init__(self, english, math, science):
        #  English = E
        self.english = english
        #  Math = M
        self.math = math
        #  Science = S
        self.science = science
    def english_grade(self):
        print(f"\t\tYour English grade is {self.english}%")
    def math_grade(self):
        print(f"\t\tYour Math grade is {self.math}%")
    def science_grade(self):
        print(f"\t\tYour Science grade is {self.science}%")

# JADEN, Make sure you change these to variables

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
        #  She reponds
        print(f"I see...")
    print("Just one moment please.")
    #  player has to type anything to progress
    #  Makes it feel as if you are waiting and breaks up the many text boxes
    input("\t\tpress enter to continue")
    #  Shows that she is actually doing something
    print("\tShe clicks her mouse and shuffles through papers")
    input("\t\tpress enter to continue")
    input("\t\tpress enter to continue")
    print(f"Well {name.upper()},")
    #  YOU ARE IN SCHOOL NOW YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH
    print(f"I'm glad to say that you are enroled in Sheetie school!")
    input("\t\tpress enter to continue")
    print("Here are your classes.")
    paper = input("\ttype 'paper' to view your classes ").lower()
    #  Lets the player make their first choice
    if paper == "paper":
        print(" Peroid 1 is English\n Peroid 2 is Math\n Peroid 3 is Science")
    else:
        print("Well you will have to look at it at some point")
    print(f"Do not be late please.")
    input("\t\tpress enter to continue")

#  Player names themselves
the_intro("So your name is...")

#  Imports the introduction menu with the logo and title screen
import Menu

#  Makes it so the players name is always upper case
name = name.upper()
input()

"""And it begins"""
print("""
    =====================================================================
    ------------------------------- DAY 1 -------------------------------
    =====================================================================
""")

#  Shows the grades of the player before each day
your_grades = Grades(0, 0, 0)
your_grades.english_grade()
your_grades.math_grade()
your_grades.science_grade()

#  Creates the setting of the game, how you are exposed to this new enviornment
print("You walk in the school")
print("A sea of students is all you can see")
input("\t\tpress enter to continue")
print("You stand there not knowing what to do until you remember...")
print("You have a backpack!")

#  Opens a loop
userinput = "IDK"
input()

#  Allows for user input for the inventory
while userinput != "quit":
    #  Shows the inventory to the player
    print("THIS IS YOUR INVENTORY")
    for item in Inventory:
        print(f"\t{item.upper()}")
    print("Type name of each item to see their values")
    print("You can still press 'quit'")
    userinput = input().lower()
    #  this line makes eberything easier to read
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    if userinput == "gum":
        #  Lets the player have gum if they want
        print(f"\tYou have {gum_total} pieces left")
        print("DO YOU WANT A PIECE?")
        print("Type 'yes' or 'no'")
        userinput = input().lower()
        #  Shows when they have no gum
        if gum_total == 0:
            print("You have no more gum, good job")
        #  Allows the user to eat the gum
        elif userinput == "yes":
            gum_total = gum_total - 1
            print(f"\tYou have {gum_total} pieces left")
            gum_out_come = randint(1, 3)
            if gum_out_come == 1:
                print("It was a bad piece, it tasted terrible")
                input("\t\tpress enter to continue")
            elif gum_out_come == 2:
                print("Tasted pretty good, not bad")
                input("\t\tpress enter to continue")
            elif gum_out_come == 3:
                print("You blew a bubble and it popped all over your face")
                input("\t\tpress enter to continue")
        elif userinput == "no":
            print("GOOD CHOICE")
        #  The player can quit at any time
        elif userinput == "quit":
            print("Thanks for playing")
        #  Shows when an input doesn't make sense
        else:
            print(f"\t\t**Invalid input**   Press 'enter'")
            input("\t\tpress enter to continue")
    #  Shows how much the player has in their wallet
    elif userinput == "wallet":
        #  My lucky number
        wallet = 12.27
        print(f"You have ${wallet} in your wallet")
        input("\t\tpress enter to continue")
    #  Lets you see whats inside your backpack
    elif userinput == "backpack":
        #  This is inside your backpack
        print("This is inside your backpack")
        print(f"\tBINDER")
        print(f"\tMAP")
        print(f"\tLUNCH")
        userinput = input().lower()
        #  Shows your binder that has your notes
        if userinput == "binder":
            print("You have no notes yet")
            input("\t\tpress enter to continue")
        #  Shows what you brought for lunch, changes everyday
        elif userinput == "lunch":
            print("YOU HAVE A LUNCH!")
            print("\tTurkey sandwich with mayo and lettuce")
            print("\tCut and washed strawberries")
            print("\tA granola bar - the chocolate chip kind")
            print("\tAnd a juice box of strawberry and kiwi")
            #  Sounds good, yummy
            input("\t\tpress enter to continue")
        #  Shows the map of the school, based on coordinates
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
            print("\tP = Entrace, Where the player STARTS")
            print("DO YOU WANT TO START WALKING?")
            #  The player gets to decide when to start the walking phase
            print("\t type 'yes' or 'no'")
            userinput = input().lower()
            if userinput == "yes":
                # Tells player the comands when walking
                userinput = "quit"
                variable_name = "yes"
            elif userinput == "no":
                print("You will have to sooner or later to progress")
                print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            #  Shows when input is wrong
            else:
                print(f"\t\t**Invalid input**   Press 'enter'")
                input("\t\tpress enter to continue")
        #  You get it at this point, I'll stop describing it
        else:
            print(f"\t\t**Invalid input**   Press 'enter'")
            input("\t\tpress enter to continue")
    #  Lets the player quit at anytime
    elif userinput == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**   Press 'enter'")
        input("\t\tpress enter to continue")


"""Code for the walking portion of the game"""
def walking(E1, E2, A1, A2, F1, F2, S1, S2, congrats, classs):
    walking_direction = "not_quit"
    #  Where the coordinates of the player come in
    global x
    global y
    while walking_direction != "quit":
        #  Shows the objective
        print(f"Objective - Get to {classs} class")
        print("THESE ARE YOUR COORDINATES")
        print(f"\t{x}, {y}\n")
        walking_direction = input("type a direction ").lower()
        #  Allows player to move up
        if walking_direction == "up":
            y = y - 1
            if y == 1:
                y = y + 1
                print("You have ran into a wall, good job!")
            elif x == E1 and y == E2:
                print(congrats)
                walking_direction = "quit"
            #  States the restrictions of the player for movement
            #  I know, I'm sorry but I couldn't
            elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 3 and y == 5) or (x == 3 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 7 and y == 5) or (x == 7 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == A1 and y == A2) or (x == F1 and y == F2):
                print("Wrong class dummy")
        #  Allows player to move down
        elif walking_direction == "down":
            y = y + 1
            if y == 7:
                y = y - 1
                print("You have ran into a wall, good job!")
            elif x == E1 and y == E2:
                print(congrats)
                walking_direction = "quit"
            #  States the restrictions of the player for movement
            elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 3 and y == 5) or (x == 3 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player for movement
            elif (x == 7 and y == 5) or (x == 7 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  Shows when the player reaches the wrong classroom
            elif (x == A1 and y == A2) or (x == F1 and y == F2):
                print("Wrong class dummy")
        #  Allows player to move left
        elif walking_direction == "left":
            x = x - 1
            if x == 1:
                x = x + 1
                print("You have ran into a wall, good job!")
            elif x == E1 and y == E2:
                print(congrats)
                walking_direction = "quit"
            #  States the restrictions of the player
            elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 3 and y == 5) or (x == 3 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 7 and y == 5) or (x == 7 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  Shows when the player reaches the wrong classroom
            elif (x == A1 and y == A2) or (x == F1 and y == F2):
                print("Wrong class dummy")
        #  Allows player to move right
        elif walking_direction == "right":
            x = x + 1
            if x == 9:
                x = x - 1
                print("You have ran into a wall, good job!")
            elif x == E1 and y == E2:
                print(congrats)
                walking_direction = "quit"
            #  States the restrictions of the player
            elif (x == 2 and y == 3) or (x == 3 and y == 3) or (x == 4 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 6 and y == 3) or (x == 7 and y == 3) or (x == 8 and
                y == 3):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 3 and y == 5) or (x == 3 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  States the restrictions of the player
            elif (x == 7 and y == 5) or (x == 7 and y == 6):
                print("You ran into another wall, good job")
                print("Because of that, you are going back to the start")
                x = S1
                y = S2
            #  Shows when the player reaches the wrong classroom
            elif (x == A1 and y == A2) or (x == F1 and y == F2):
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
            print(f"\t\t**Invalid input**   Press 'enter'")

#  Shows the commands of the walking portion so the player knows how to play
while variable_name == "yes":
    print("TYPE A COMMAND")
    print("\t'up' to go up")
    print("\t'down' to go down")
    print("\t'left' to go left")
    print("\t'right' to go right")
    print("\t'quit'")
    print("\t'map' to view the map again")
    #  Doesn't matter what the player responds with
    input("Did you get all that? \n")
    variable_name = "no"
    walking(2, 6, 2, 2, 8, 2, 5, 6, "Nice, you got to class, shocking",
            "English")
    English_class = "active"

#  First class for the player, yes notes need to be taken down
while English_class != "quit":
    input()
    print("You enter the classroom, every desk is filed.")
    print(f"Hello {name}! Please take a seat.")
    input("\tYou take a seat")
    print("Alright class, we are going to start off the day with notes.")
    print("I know you guys love doing them")
    #  The player must rewrite the notes that are being given from the teacher
    print("Now class, begin writing as soon as I do")
    print("\t\tPoems -- Poems are collections of words that express")
    print("\t\tan idea or emotion that often use imagery and metaphor.")
    Enotes_1 = input().lower()
    print("\nI hope you can follow along class, I write fast")
    input()
    print("\t\tAs you are studying literature, you will likely notice")
    print("\t\tthat poems come in many different forms.")
    Enotes_2 = input().lower()
    print("\t\tAs you read and perhaps write your own poems, it is helpful to")
    print("\t\tknow the different kinds of poems.")
    Enotes_3 = input().lower()
    print("Your new notes will be placed in your binder")
    #  You meet someone!!
    (print("\n\tA RANDOM ENCOUNTER HAS OCCURED"))
    English_class = "quit"
    other_variable_name = "not_quit"

#  This portion is your interaction between the player and this new character
while other_variable_name != "quit":
    print("Man, isn’t this school big? I could barely find my class in time")
    #  Shows the options of the player
    print("\tChoose - ‘Friendly'")
    print("\t\t - ’Hostile’\n\t\t - ‘Too friendly’\n\t\t - ‘Say nothing’")
    choice = input().lower()
    #  Shows the friendly route
    if choice == "friendly":
        print("I know right, it’s too big and nobody even showed me around")
        print(f"My name is {name}, what’s yours?")
        print("I'm Jim")
        input("press enter to continue")
        other_variable_name = "quit"
        print("RIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGG")
        print("Oh no, we will have to pick this up tomorrow class. - t")
        print("\t\ttime, to get to your next class\n")
        other_userinput = "not_quit"
        your_grades.english_grade()
    #  Hostile route
    elif choice == "hostile":
        print("Bro, back off. You’ll have to find your next class on your own")
        print("Oh, alright then. I'll leave you alone.\n")
        print("\t\tHe walks away looking sad")
        input("press enter to continue")
        print("RIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGG")
        print("Oh no, we will have to pick this up tomorrow class. - t")
        print("\t\ttime, to get to your next class\n")
        other_variable_name = "quit"
        other_userinput = "not_quit"
        your_grades.english_grade()
    #  Romantic route
    elif choice == "too friendly":
        print("Is it just me or is their some kind of connection here?\n")
        print("Woah! Um, I have to go now.")
        print("\t\tHe moves to the other side of the classroom")
        input("press enter to continue")
        other_variable_name = "quit"
        print("RIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGG")
        print("Oh no, we will have to pick this up tomorrow class. - t")
        print("\t\ttime, to get to your next class\n")
        other_userinput = "not_quit"
        your_grades.english_grade()
    #  Silent route
    elif choice == "say nothing":
        print("Oh, alright then. I'll leave you alone.\n")
        print("\t\tHe walks away looking sad")
        input("press enter to continue")
        other_variable_name = "quit"
        print("RIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGG")
        print("Oh no, we will have to pick this up tomorrow class. - t")
        print("\t\ttime, to get to your next class\n")
        other_userinput = "not_quit"
        your_grades.english_grade()
    #  Still lets the player quit
    elif choice == "quit":
        print("Thanks for playing")
        other_variable_name = "quit"
    else:
        print(f"\t\t**Invalid input**   Press 'enter'")

#  Allows for user input for the inventory
while other_userinput != "quit":
    #  Shows the inventory to the player
    print("THIS IS YOUR INVENTORY")
    for item in Inventory:
        print(f"\t{item.upper()}")
    print("Type name of each item to see their values")
    print("You can still press 'quit'")
    other_userinput = input().lower()
    #  this line makes eberything easier to read
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    if other_userinput == "gum":
        #  Lets the player have gum if they want
        print(f"\tYou have {gum_total} pieces left")
        print("DO YOU WANT A PIECE?")
        print("Type 'yes' or 'no'")
        other_userinput = input().lower()
        #  Shows when they have no gum
        if gum_total == 0:
            print("You have no more gum, good job")
        #  Allows the user to eat the gum
        elif other_userinput == "yes":
            gum_total = gum_total - 1
            print(f"\tYou have {gum_total} pieces left")
            gum_out_come = randint(1, 3)
            if gum_out_come == 1:
                print("It was a bad piece, it tasted terrible")
                input("\t\tpress enter to continue")
            elif gum_out_come == 2:
                print("Tasted pretty good, not bad")
                input("\t\tpress enter to continue")
            elif gum_out_come == 3:
                print("You blew a bubble and it popped all over your face")
                input("\t\tpress enter to continue")
        elif other_userinput == "no":
            print("GOOD CHOICE")
        #  The player can quit at any time
        elif other_userinput == "quit":
            print("Thanks for playing")
        #  Shows when an input doesn't make sense
        else:
            print(f"\t\t**Invalid input**   Press 'enter'")
            input("\t\tpress enter to continue")
    #  Shows how much the player has in their wallet
    elif other_userinput == "wallet":
        print(f"You have ${wallet} in your wallet")
        input("\t\tpress enter to continue")
    #  Lets you see whats inside your backpack
    elif other_userinput == "backpack":
        #  This is inside your backpack
        print("This is inside your backpack")
        print(f"\tBINDER")
        print(f"\tMAP")
        print(f"\tLUNCH")
        other_userinput = input().lower()
        #  Shows your binder that has your notes
        if other_userinput == "binder":
            print(Enotes_1)
            print(Enotes_2)
            print(Enotes_3)
            input("\t\tpress enter to continue")
        #  Shows what you brought for lunch, changes everyday
        elif other_userinput == "lunch":
            print("YOU HAVE A LUNCH!")
            print("\tTurkey sandwich with mayo and lettuce")
            print("\tCut and washed strawberries")
            print("\tA granola bar - the chocolate chip kind")
            print("\tAnd a juice box of strawberry and kiwi")
            #  Sounds good, yummy
            input("\t\tpress enter to continue")
        #  Shows the map of the school, based on coordinates
        elif other_userinput == "map":
            #  prints map with borders
            print("<><><><><><><><><><><><><><>")
            for layer in Layers:
                print(*layer, sep='')
            print("<><><><><><><><><><><><><><>")
            #  Prints Legend
            print("\tE = English class")
            print("\tM = Math class")
            print("\tS = Science class")
            print("\tP = Entrace")
            print("Still all the same")
            print("DO YOU WANT TO START WALKING AGAIN?")
            #  The player gets to decide when to start the walking phase
            print("\t type 'yes' or 'no'")
            other_userinput = input().lower()
            if other_userinput == "yes":
                # Tells player the comands when walking
                other_userinput = "quit"
                walking(2, 2, 8, 2, 0, 0, 2, 6,
                        "Great, you seem to know what your doing now.", "Math")
            elif other_userinput == "no":
                print("You will have to sooner or later to progress")
                print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            #  Shows when input is wrong
            else:
                print(f"\t\t**Invalid input**   Press 'enter'")
                input("\t\tpress enter to continue")
        #  You get it at this point, I'll stop describing it
        else:
            print(f"\t\t**Invalid input**   Press 'enter'")
            input("\t\tpress enter to continue")
    #  Lets the player quit at anytime
    elif other_userinput == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**   Press 'enter'")
        input("\t\tpress enter to continue")

"""Coordinates for each class, you can ignore this"""
#  E = 2, 6
#  A = 2, 2
#  F = 8, 2
#  P = 5, 6

print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
input()
print("Hey, I just want to say thank you for making it this far.")
print("I know it wasn't super long, I intended it to be significantly longer")
print("Hopefully it will be done by next semester:)")
