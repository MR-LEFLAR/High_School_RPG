#  Name: Jaden Leflar
#  Period: 4
#  Course: CS30
#  Date created: 07/01/20
#  Description: RPG Simple Menu start up

#  Shows the titles
print("""
--------------------------WELCOME TO VIRTUAL HELL---------------------
-----------------------------AKA SHEETIE SCHOOL-----------------------
  """)

#  Creates a book out of characters on the keyboard
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
        #  Letting the player actually interact with the game
        print("Type 'start' to begin")
        print("Type 'quit' to end the program")
        a = input().lower()
        if a == "start":
            #  Shows the instructions
            print("\t-------Here are the instructions-------")
            print("\tVarious stages of the game have different controls")
            print("\tYou will be told what you can and cannot type\n")
            print("\tType 'quit' at any point to leave the game")
            print("\ttype 'lets do this' to begin")
            #  Lets the text get divided
            starter = input().lower()
            if starter == "lets do this":
                #  Ends the loop
                a = "quit"
                #  Fair warning
                print("Well, you are probably going to regret this")
                # Seperates the many texts
                input()
                input("Here it comes!")
            elif "starter" == "quit":
                #  Allows the player to quit at any time
                print("Thanks for playing")
            else:
                #  Points out if the command given is valid or not
                print("Invalid command")
        elif a == "quit":
            #  Allows the player to quit at any time
            print("Thanks for playing")
        else:
            #  Points out if the command given is valid or not
            print(f"\t\t**Invalid input**")

#  Calls the function
menu("null", "quit")
