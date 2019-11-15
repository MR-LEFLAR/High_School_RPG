# Name: Jaden Leflar
# Period: 4
# Course: CS30
# Date created: 15/11/19
# Description: Map

# To add a layer to the map, draw another layer using the same format,
#and reference in yaxislist. These are the only 2 references necessary.
yaxis0 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' M ']
yaxis1 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis2 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis3 = [' . ',' P ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis4 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis5 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis6 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']
yaxis7 = [' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ']

 #creates a multidimensional array
yaxislist = [yaxis0, yaxis1, yaxis2, yaxis3, yaxis4, yaxis5, yaxis6, yaxis7]
minyaxis = len(yaxislist)-1 # finds the value of the lowest y-axis

# variable incantations
userin = "setup placeholder"
global searchinterval, xaxis, yaxis
oldev = ' . '
ev = ' . '
searchinterval = 0
yaxis = 0
activeyaxis = yaxis0
tempyaxis = yaxis0

# sets up axisfinder, a function which locates the X on the grid
def axisfinder():
    global searchinterval, xaxis, yaxis # recieves globals
    xnotfound = True # sets boolean to false
    searchinterval = 0 # resets searchinterval
    yaxis = 0 # resets yaxis
    xaxis = 0 # resets xaxis
    while xnotfound and searchinterval <= 1000: # sets while criteria
        try: #if it can run the following:
            # sets P to be equal to the index of the currently searched list
            xaxis = yaxislist[searchinterval].index(' P ')
            yaxis = searchinterval # yaxis is equal to currently searched yaxis
            xnotfound = False # boolean set to false to cancel while
        except: # if the previous could not be run:
            searchinterval = searchinterval + 1 #add 1 to search interval

# prints the world map with a revieved value of the minimum yaxis to be printed
def worlddisplay(minyaxisnum):
    interval = 0 #incantates interval
    print("[][][][][][][][]") # prints a border
    # while the interval is smaller than the accepted value:
    while interval <= minyaxisnum:
        print(*yaxislist[interval], sep='') #print the yaxis w/o any list stuff
        interval = interval + 1 # add 1 to interval
    print("[][][][][][][][]") # prints a vibing border

def eventfinder(eventcode):
    if eventcode == ' . ':
        if "w" in userin or "s" in userin: #only runs next lines if met
            tempyaxis.insert(xaxis, ' P ') # if going up or down insert a new P
            del activeyaxis[xaxis] # delete old P
        activeyaxis.insert(xaxis, oldev) # insert the missing map part
        worlddisplay(minyaxis) # draw the map
    if eventcode == ' M ':
        if "w" in userin or "s" in userin:# only runs next lines if met
            tempyaxis.insert(xaxis, ' P ')# if going up or down insert a new P
            del activeyaxis[xaxis]# delete old P
        activeyaxis.insert(xaxis, oldev)# insert the missing map part
        worlddisplay(minyaxis)# draw the map
        print("you made it to class! congratulations!")

worlddisplay(minyaxis) # initial display function, for initialization

while userin != "quit": # consistently run the following
    userin = input().lower() # take user input in lower case
    axisfinder() # find the P
    activeyaxis = yaxislist[yaxis] # set the activeyaxis to the yaxis with P

    elif userin == "axistest": # used for testing again, n/a
        axisfinder()
        print("yaxis: " + str(yaxis))
        print("xaxis: " + str(xaxis))
    else: # run if the input is not in range of anything prior
        worlddisplay(minyaxis) # draw map
        print("Invalid input") # print invalid input to console
