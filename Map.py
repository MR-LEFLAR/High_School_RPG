# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 15/11/19
# Description: Map

#Imports other modules
import Nested_Dic
userinput= "Blank"

# Prints out the map that is visilble to the player
layer1 = [' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
layer2 = [' | ',' M ',' . ',' . ',' . ',' . ',' . ',' S ',' | ']
layer3 = [' | ',' _ ',' _ ',' _ ',' . ',' _ ',' _ ',' _ ',' | ']
layer4 = [' | ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' | ']
layer5 = [' | ',' . ',' | ',' . ',' . ',' . ',' | ',' . ',' | ']
layer6 = [' | ',' E ',' | ',' . ',' . ',' . ',' | ',' . ',' | ']
layer7 = [' | ',' _ ',' _ ',' _ ',' P ',' _ ',' _ ',' _ ',' | ']

# Inputs layers into a list
Layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7]

# Allows for user imput
while userinput != "quit":
    # For now, only allows player to look at map
    print("type 'map' to look at map")
    print("type 'legend' to know what the map means")
    # Tells the player can quit at any time
    print("Press 'quit' to end the game")
    userinput = input().lower()
    if userinput == "map":
        # prints map with borders
        print("<><><><><><><><><><><><><><>") # prints border
        for layer in Layers:
            print(*layer, sep='')
        print("<><><><><><><><><><><><><><>") # prints border
    elif userinput == "legend":
        # Prints Legend
        print("\tE = English class")
        print("\tM = Math class")
        print("\tS = Science class")
        print("\tP = Entrace, Where the player starts")
    elif userinput == "quit":
        print("Thanks for playing")
    else:
        print("Invalid input")
