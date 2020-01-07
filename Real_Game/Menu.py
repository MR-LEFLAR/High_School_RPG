# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 29/10/19
# Description: RPG Simple Menu start up

# Shows the titles
print("""
--------------------------WELCOME TO VIRTUAL HELL---------------------
-----------------------------AKA SHEETI SCHOOL------------------------
  """)

# Creates a book out of characters on the keyboard
print("""
                          ______ ______
                        _/      Y      \_
                       // ~~ ~~ | ~~ ~  \\
                      // ~ ~ ~~ | ~~~ ~~ \\
                     //________.|.________\\
                    '----------`-'----------'
  """)

def menu(a, b):
    while a != "quit":
        # Letting the player actually interact with the game
        print("Type 'start' to begin")
        print("Type 'quit' to end the porgram")
        a = input().lower()
        if a == "start":
            # Shows the instructions
            print("\t-------Here are the instructions-------")
            print("\tVarious stages of the game have different controls")
            print("\tYou will be told what you can and cannot type\n")
            print("\tType 'quit' at any point to leave the game")
            print("\ttype 'lets do this' to begin")
            a = "quit"
            # Lets the text get divided
            input()
        elif a == "quit":
            # Allows the player to quit at any time
            print("Thanks for playing")
        else:
            # Points out if the command given is valid or not
            print("Invalid command")

# Calls the function
menu("null", "quit")
