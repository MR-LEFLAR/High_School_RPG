# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 29/10/19
# Description: RPG Simple Menu start up

starting_up = 1
a = "not_null"
menu = 0

if starting_up == 1:
    print("---------------------WELCOME TO VIRTUAL HELL---------------------")
    print("-------------------------AKA High School-------------------------")
    print("""
                              ______ ______
                            _/      Y      \_
                           // ~~ ~~ | ~~ ~  \\
                          // ~ ~ ~~ | ~~~ ~~ \\
                         //________.|.________\\
                        `----------`-'----------' """)
    starting_up = 0
    a = "null"

if a == "null":
    print("Type 'start' to begin")
    a = input()
    if a == "start":
        print("\t----Here are the instructions----")
        print("\tVarious stages of the game have different controls")
        print("\tYou will be told what you can and cannot type\n")
        print("\tType 'quit' at any point to leave the game")
        print("\ttype 'lets do this' to begin")
        menu = input()

if a != "null" or "start":
    print("Invalid command")
    print("Type 'start' to begin")
    a = input()

if menu == "lets do this":
    print("=================================================================")
    print("----------------------------- DAY 1 -----------------------------")
    print("=================================================================")
if menu != "Lets do this" or "quit":
    print("Invalid command")
    print("Type 'lets do this' to begin")
    print("Type 'quit' to leave the game")
    menu = input()

if menu == "quit":
    print("Thanks for playing!")
