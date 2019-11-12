# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 29/10/19
# Description: RPG Simple Menu start up

# Shows the titles
print("""
--------------------------WELCOME TO VIRTUAL HELL---------------------
------------------------------AKA High School-------------------------
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
            b = "not_quit"
            a = "quit"
        elif a == "quit":
            # Allows the player to quit at any time
            print("Thanks for playing")
        else:
            # Points out if the command given is valid or not
            print("Invalid command")

    while b != "quit":
        b = input().lower()
        if b == "lets do this":
            # Start of day one, the actual game
            print("""
        =====================================================================
        ------------------------------- DAY 1 -------------------------------
        =====================================================================
              """)
            b = "quit"
        elif b == "quit":
            # Allows the player to quit at any time
            print("Thanks for playing")
        else:
            # Points out if the command given is valid or not
            print("Invalid command")
            print("Type 'lets do this' to begin")
            print("Type 'quit' to leave the game")

# Calls the function
menu("null", "quit")
