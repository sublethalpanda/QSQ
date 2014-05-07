from random import randint
from Combat import combat
from Gnoblin import Gnoblin
import Globals
position = [2,1]
mapQuitFlag = False

def positionCheck():
    return position

def mapMain(userIn):
    global mapQuitFlag
    userIn = userIn[0:1]
    checkDirect(userIn)
    if not Globals.player.dead():
        roomDesc(position[0],position[1])

def room(x,y,direc):
    global flag
    position = [x,y]
    if position == [2,0]:
        #Exit
        print("You exit the cave")
        #Globals.gameState = "Running"
        Globals.quitGame = True
        flag = True
        return True
    elif position == [2,1]:
        return True
    elif position == [3,0]:
        return True
    elif position == [0,1]:
        return True
    elif position == [1,1]:
        return True
    elif position == [3,1]:
        return True
    elif position == [4,1]:
        return True
    elif position == [5,1]:
        return True
    elif position == [1,2]:
        return True
    elif position == [2,2]:
        return True
    elif position == [4,2]:
        return True
    elif position == [0,3]:
        if direc !="w":
            return False
        else:
            return True
    elif position == [1,3]:
        if direc == "w":
            return False
        else:
            if Globals.whaleTrap == False:
                Globals.whaleTrap = True
                if randint(1,20)+Globals.player.DEX >= 20:
                    print("\nYou narrowly dodge a large form falling from the ceiling.\nA whale has fallen to the ground, covering the walls with bits of Baleen.")
                else:
                    tempDamage = randint(1,200)+50+randint(1,Globals.player.HP[1] - 1)
                    print("\nYou are hit by a whale falling from the ceiling for",tempDamage,"damage.")
                    Globals.player.HP[0] -=tempDamage
                    if Globals.player.dead():
                        print("Game Over...")
                        Globals.quitGame = True
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
        if Globals.getKey == False:
            print("There is a key here.")
        if direc == "n":
            return False
        else:
            return True
    elif position == [1,4]:
        if direc == "w":
            return False
        else:
            if Globals.miniBoss == False:
                combat([Globals.player, Gnoblin(Globals.levelInit+25)])
                Globals.miniBoss = True
            return True
    elif position == [2,4]:
        print("This is the resting room")
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
        if Globals.doorUnlocked == True:
            if Globals.defeatBoss == False:
                combat([Globals.player, Gnoblin(Globals.levelInit+60)])
                Globals.defeatBoss = True
            return True
        else:
            print("You need a key to unlock this door!")
            return False
    else:
        return False
    return True

def roomDesc(x,y):
    descList = [[None,None,"\nThe sun shines warmly on your face.","\nYou have entered a dead-end.\nThis ornate purple room has a single exit to the North."],["\nYou have reached a dead-end.\nBeyond you lies a wall made of stone.","\nYou are at the southwest side of the pillar.\nA small tunnel leads west, while the main causeway runs East and North.","\nYou are in the main entrance of the cave.\nLight spills in from the southern exit, while a great pillar stands to\nyour northwest, yielding both north and west passageways.\nA hall heads East of here as well.","\nThe hall continues, with a smaller passageway branching off to the south.","\nThe hall continues forward and is joined by a\nlarger, crimson hall running North.","\nThe hall ends here, with a portrait that looks much like you.\nIf you knew what you looked like."],[None,"\nYou are at the northwest section of the pillar.\nPassageways branch north, south, and east.","\nYou are at the northeast section of the pillar.\nYou feel a warm breeze move through the cave here, soothing you.\nPathways lead North,South,and West from here.",None,"\nThe hall becomes a truer hue of crimson, and\nornate gold lones paint the ceiling above you."],["""You have found the Cartographer's Room!
          O         T
          |         |
     O----O----O    O
     |         |    |
O----M    R    O    O
     |    |    |    |
C----O    O----O    O
     |    |         |
     O----O         O
     |    |         |
O----O----O----O----O----O
          |    |
          X    O
This is painted on one of the walls.
    ""","\nThe air around you smells of old sushi and stale Baleen Bits.\nPathways lead North, South, and West.","\nYou can feel a warmth from the North.\nThe path splits off here, going from a n/s hall to an eastward tunnel.","\nThe tunnel grows dim and heads North and West.","\nYou feel a chill go down your spine as you continue through the dim hallway."],["\nYou are in a small room with a pedestal.","\nYou are in a large antechamber filled halfway with water.","\nYou are in the resting room. A small ever-burning fire warms the floor,\nwhich is covered with a soft, snow-white layer of grass.","\nThe tunnel continues North and South.","\nYou can see a large red door far ahead of you.\nThe hall continues."],[None,"\nThe pathway turns sharply.\nPaths are to the East and South.","\nThere is a junction to the North here.","\nThe air around you smells of something or other.\nThe path from the West continues South as a rough cave.","\nYou are at the bright red door."],[None,None,"\nNothing here.\n\nOther than you, of course.",None,"\nYou are in the dragon's den!"]]
    print(str(descList[y][x]))

def checkDirect(userIn):
    global position
    blockFlag = False
    if userIn == "n":
        if room(position[0],position[1]+1,userIn):
            position[1] += 1
        else:
            blockFlag = True
    elif userIn =="s":
        if room(position[0],position[1]-1,userIn):
            position[1] -= 1
        else:
            blockFlag = True
    elif userIn =="e":
        if room(position[0]+1,position[1],userIn):
            position[0] += 1
        else:
            blockFlag = True
    elif userIn =="w":
        if room(position[0]-1,position[1],userIn):
            position[0] -= 1
        else:
            blockFlag = True
    else:
        print("That is not a direction!")
    if blockFlag == True:
        print("You can't go that way!")
    else:
        if randint(1,3) == 1 and position != [2,0] and position!= [1,4] and position != [4,6] and position !=[2,4]:
            combat([Globals.player, Gnoblin(min(randint(15,25),max(1, randint(Globals.player.level - 5, Globals.player.level + 5)))+Globals.levelInit )])
