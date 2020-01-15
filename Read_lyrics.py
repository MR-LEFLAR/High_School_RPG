#  Name: Jaden Leflar
#  Period: 4
#  Course: CS30
#  Date created: 15/01/20
#  Description: Printing Song Lyrics

with open("Lyrics.txt") as file_object:
    contents = file_object.read()
print(contents.rstrip())
