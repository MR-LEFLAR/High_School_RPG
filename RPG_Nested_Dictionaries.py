# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 25/10/19
# Description: RPG Nested Dictionaries


def thingy(Name):
    # prints out the items, keys, and values in the Dictionaries
    for Name, key in Name.items():
        # Does a loop through the dictionaies and prints all their contents
        print(Name + ":")
        for items in key:
            # Goes through the nested dictionaries and prints their contents
            print(f"\t{items} - {key[items]}")

# who is the main character and what are his traits
main_character = {
        "Main character": {
        "Name": "*@#$!&%^/",
        "Age": 14,
        "Grade": 9,
        "Personality": "depends on player choices"}
}

# All the other characters shown in the game
side_characters = {
        "Side characters": {
        # In order of apperence
        "mom": "mother of main character",
        "period 1 teacher": "English teacher, Mrs. C",
        "Jake": "possible friend or enemy(depends on player)",
        "Roger": "school bully, will always be an enemy",
        "period 2 teacher": "strict science teacher, Mr. Hateskids",
        "period 3 teacher": "Fast paste math teacher, Mrs. O",
        "Kate": "The girl who cheats on tests, can be friend or enemy"}
}

# Various locations within the school and the school itself
locations = {
        "Locations": {
        "School": "Only location in the game, where the player roams",
        "Period 1": "English class, may have to read or write notes",
        "Period 2": "Science class, taking tests and doing experiments",
        "Period 3": "Math class, lots of tests with real math questions"}
}

# Inventory prompt that the player can choose what they want
Inventory = {
        "Gum": {"Total pieces left": 10},
        "Wallet": {"Total cash": "$12.27"},
        "Backpack": {"Binder": "Used to refer to notes for tests",
        "Pencil": "Used to write tests and notes, can have more than one",
        "Eraser": "Used to erase tests and notes, can have more than one",
        "Lunch": "Can be eaten at any time"}
            }

# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE MAIN CHARACTER")
thingy(main_character)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE SIDE CHARACTERS")
thingy(side_characters)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE LOCATIONS")
thingy(locations)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE INVENTORY")
thingy(Inventory)
# Makes it easier to read
print("------------------------------------------------------------------")
