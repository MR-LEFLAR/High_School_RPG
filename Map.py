# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 15/11/19
# Description: Using th Python Standard Library

# Imports random variable generator
from random import randint

# Creates a place holder for the main variable
userinput= "Blank"
walking_direction = "Blank"
# Creates the Inventory that will be used in game
Inventory = {
        "Gum": {"Total pieces left": 10},
        "Wallet": {"Total cash": "$12.27"},
        "Backpack": {"Binder": "Used to refer to notes for tests",
        "Pencil": "Used to write tests and notes, can have more than one",
        "Eraser": "Used to erase tests and notes, can have more than one",
        "Lunch": "Can be eaten at any time",
        "Map": "Can be used to see where classes are"}
            }

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

# Allows for user imput
while userinput != "quit":
    # Shows the inventory to the player
    print("This is your INVENTORY")
    for item in Inventory:
        print(f"\t{item.upper()}")
    print("Type name of each item to see their values")
    print("Type 'back' to exit a menu")
    print("Press 'quit' to end the game")
    userinput = input().lower()
    # Makes it easier to read
    print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    if userinput == "gum":
        # Uses the Python Standard Library of a random variable
        x = randint(1, 10)
        print(f"\tYou have {x} pieces left")
        print("Type 'eat' to eat")
        userinput = input().lower()
        # Shows when they have no gum
        if x == 0:
            print("You have no more gum, good job")
        # Allows the user to eat the gum
        elif userinput == "eat":
            x = x - 1
            print(f"You have {x} pieces left")
        # The player can quit at any time
        elif userinput == "quit":
            print("Thanks for playing")
        # Can go back on menus
        elif userinput == "back":
            print(f"You still have {x} pieces left")
            # Shows when the input is not valid
        else:
            print(f"\t\t**Invalid input**")
    elif userinput == "wallet":
        wallet = 12.27
        print(f"You have ${wallet} in your wallet")
    elif userinput == "backpack":
        # This is inside your backpack
        print("This is inside your backpack")
        print(f"\tBINDER")
        print(f"\tMAP")
        print(f"\tLUNCH")
        userinput = input().lower()
        if userinput == "binder":
            print("just notes in here, you don't need to look at them")

        elif userinput == "map":
            # prints map with borders
            print("<><><><><><><><><><><><><><>") # prints border
            for layer in Layers:
                print(*layer, sep='')
            print("<><><><><><><><><><><><><><>") # prints border
            # Prints Legend
            print("\tE = English class")
            print("\tM = Math class")
            print("\tS = Science class")
            print("\tP = Entrace, Where the player starts")
    elif userinput == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**")

while walking_direction != quit:
    x = 5
    y = 7
    if (x == 4 and y == 7):
        print("You have run into a wall, good job!")
    if userinput == "up":
        y = y - 1
        print(f"\t{x}, {y}")
    elif userinput == "down":
        y = y + 1
        print(f"\t{x}, {y}")
    elif userinput == "left":
        x = x - 1
        print(f"\t{x}, {y}")
    elif userinput == "right":
        x = x + 1
        print(f"{x}, {y}")
    # The player can quit at any time
    elif userinput == "quit":
        print("Thanks for playing")
    else:
        print(f"\t\t**Invalid input**")
