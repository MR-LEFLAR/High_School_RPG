"""A file with the purpose of testing different code types
does not have anything to do with the game"""

def post_float(message):
    """Test for checking if an input is a positive float"""
    # the while loop makes sure the program continues until the user
    # has inputted a valid number
    while True:
        # the try statement attempts tp exceute the user input
        try:
            userInput = float(input(message))
            # The if-else statement tests to see if the number is positive
            # if the number is positive then the program continues
            if userInput > 0:
                return userInput
            # if the number is not positive then the user must
            # input a new number
            else:
                print("Not a positive number. Try again.")
                continue
        # if the user did not input a number, the user is prompted to try again
        except ValueError:
            print("Input is not a number. Try again.")
            continue

post_float("Give me a positive number ")
