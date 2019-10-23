# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 25/10/19
# Description: RPG Nested Dictionaries

# who is the main character and what are his traits
main_character = {
        # He does not have a name because it is the player
        "Name": "*@#$!&%^/",
        "Age": 14,
        "Grade": 9,
        "Personality": "depends on player choices"
}

# All the other characters shown in the game
side_characters = {
        # In order of apperence
        "mom": "mother of main character",
        "period 1 teacher": "English teacher, Mrs. C",
        "Jake": "possible friend or enemy(depends on player)",
        "Roger": "school bully, will always be an enemy",
        "period 2 teacher": "strict science teacher, Mr. Hateskids",
        "period 3 teacher": "Fast paste math teacher, Mrs. O",
        "Kate": "The girl who cheats on tests, can be friend or enemy"
}

# Combining the two dictionaries into a list
characters = [main_character, side_characters]

# Printing the charcater names and descriptions
for character in characters:
    print(character)
    # Makes it easier to read
    print("--------------------------------------------------------------")

# Various locations within the school and the school itself
locations = {
        "School": "Only location in the game, where the player roams",
        "Period 1": "English class, may have to read or write notes",
        "Period 2": "Science class, taking tests and doing experiments",
        "Period 3": "Math class, lots of tests with real math questions",
}

# Printing the locations
print(locations)
# Makes it easier to read
print("--------------------------------------------------------------")

# Inventory prompt that the player can choose what they want
Inventory = {
        "Gum": "Can be eaten or given out, people like gum",
        "School_Map": "Used to navigate your way through the school",
        "Wallet": "Shows the money you have, can buy snacks or give out",
        "Backpack": {"Binder": "Used to refer to notes for tests",
        "Pencil": "Used to write tests and notes, can have more than one",
        "Eraser": "Used to erase tests and notes, can have more than one",
        "Lunch": "Can be eaten at any time"}
}

# Printing the Inventory
print(Inventory)
# Makes it easier to read
print("------------------------------------------------------------------")
