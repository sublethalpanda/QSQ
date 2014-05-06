position = [2,1]

#Test Input

def main():
    roomDesc(position[0],position[1])
    global flag
    userIn = input("\n>").lower()
    if userIn == "exit":
        print("closing...")
        flag = True
    userIn = userIn[0:1]
    checkDirect(userIn)
    print(position)

def room(x,y,direc):
    global flag
    position = [x,y]
    if position == [2,0]:
        #Exit
        print("You exit the cave")
        flag = True
        return True
    elif position == [2,1]:
        #Entrance room, N E W, S exits.
        return True
    elif position == [3,0]:
        #Offshoot
        return True
    elif position == [0,1]:
        #Offshoot
        return True
    elif position == [1,1]:
        #NEW Junction
        return True
    elif position == [3,1]:
        #SEW Junction
        return True
    elif position == [4,1]:
        #NEW Junction
        return True
    elif position == [5,1]:
        #Offshoot
        return True
    elif position == [1,2]:
        #NSE Junction
        return True
    elif position == [2,2]:
        #NSW Junction
        return True
    elif position == [4,2]:
        #NS Hall
        return True
    elif position == [0,3]:
        #Offshoot
        if direc !="w":
            return False
        else:
            return True
    elif position == [1,3]:
        if direc == "w":
            return False
        else:
            return True
    elif position == [2,3]:
        if direc == "e":
            return False
        else:
            return True
    elif position == [3,3]:
        if direc == "w":
            return False
        else:
            return True
    elif position == [4,3]:
        if direc == "e":
            return False
        else:
            return True
    elif position ==[0,4]:
        #Key Room
        if direc == "n":
            return False
        else:
            return True
    elif position == [1,4]:
        if direc == "w":
            return False
        else:
            return True
    elif position == [2,4]:
        #Rest area
        if direc == "n":
            return True
        else:
            return False
    elif position == [3,4]:
        if direc == "e" or dir == "w":
            return False
        else:
            return True
    elif position == [4,4]:
        if direc == "e":
            return False
        else:
            return True
    elif position == [1,5]:
        return True
    elif position == [2,5]:
        if direc == "n":
            return False
        else:
            return True
    elif position == [3,5]:
        if direc == "w":
            return False
    elif position == [4,5]:
        if direc == "e":
            return False
        else:
            return True
    elif position == [2,6]:
        return True
    elif position == [4,6]:
        return True
    else:
        return False
    return True

def roomDesc(x,y):
    descList = [[None,None,"20","30"],["01","11","21","31","41"],[None,"12","22",None,"42"],["03","13","23","33","43"],["04","14","24","34","44"],[None,"15","25","35","45"],[None,None,"26",None,"46"]]
    print(str(descList[y][x]))

def checkDirect(userIn):
    global position
    blockFlag = False
    if userIn == "n":
        if room(position[0],position[1]+1,userIn):
            print("Moving north")
            position[1] += 1
        else:
            blockFlag = True
    elif userIn =="s":
        if room(position[0],position[1]-1,userIn):
            print("Moving south")
            position[1] -= 1
        else:
            blockFlag = True
    elif userIn =="e":
        if room(position[0]+1,position[1],userIn):
            print("Moving east")
            position[0] += 1
        else:
            blockFlag = True
    elif userIn =="w":
        if room(position[0]-1,position[1],userIn):
            print("Moving west")
            position[0] -= 1
        else:
            blockFlag = True
    else:
        print("That is not a direction!")
    if blockFlag == True:
        print("You can't go that way!")
flag = False
print("Pick a direction. type 'exit' to leave.")
while flag == False:
    main()





