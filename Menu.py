# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 29/10/19
# Description: RPG Simple Menu start up

# Variable that decide which menu will pop up
starting_up = 1
a = "not_null"
menu = 0
b = "idk"

if starting_up == 1:
    # Shows the titles
    print("------------------------WELCOME TO VIRTUAL HELL-------------------")
    print("----------------------------AKA High School-----------------------")
    # Creates a book out of characters on the keyboard
    print("""
                              ______ ______
                            _/      Y      \_
                           // ~~ ~~ | ~~ ~  \\
                          // ~ ~ ~~ | ~~~ ~~ \\
                         //________.|.________\\
                        '----------`-'----------'
        """)
    starting_up = 0
    a = "null"

while a == "null":
    # Letting the player actually interact with the game
    print("Type 'start' to begin")
    b = input()
    if b == "start":
        # Shows the instructions
        print("\t----Here are the instructions----")
        print("\tVarious stages of the game have different controls")
        print("\tYou will be told what you can and cannot type\n")
        print("\tType 'quit' at any point to leave the game")
        print("\ttype 'lets do this' to begin")
        a = "not_null_again"
    elif b == "quit":
        # Shows that you can quit at any time
        print("Thanks for playing!")
        a = "not_null"
    elif b != "start" or "quit":
        # Tells the player to insert a valid command
        print("Invalid command")
        print("Type 'start' to begin")
        a = "null"

while a == "not_null_again":
    menu = input()
    if menu == "lets do this":
        # Start of day one
        print("=============================================================")
        print("--------------------------- DAY 1 ---------------------------")
        print("=============================================================")
        a = "not_null"
    elif menu == "quit":
        # Shows that you can quit at any time
        print("Thanks for playing!")
        a = "not_null"
    elif menu != "lets do this" or "quit":
        # Tells the player to insert a valid command
        print("Invalid command")
        print("Type 'lets do this' to begin")
        print("Type 'quit' to leave the game")
