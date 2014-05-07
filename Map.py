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
        Globals.gameState = "Running"
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
                    print("You narrowly dodge a large form falling from the ceiling.\nA whale has fallen to the ground, covering the walls with bits of Baleen.")
                else:
                    tempDamage = randint(1,200)+50
                    print("You are hit by a whale falling from the ceiling for",tempDamage,"damage.")
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
    descList = [[None,None,"The sun shines warmly on your face.","You have entered a dead-end. This ornate purple room has a single exit to the North."],["You have reached a dead-end. Beyond you lies a wall made of stone.","You are at the southwest side of the pillar. A small tunnel leads west, while the main causeway runs East and North.","You are in the main entrance of the cave. Light spills in from the southern exit, while a great pillar stands to your northwest, yielding both north and west passageways. A hall heads East of here as well.","The hall continues, with a smaller passageway branching off to the south.","The hall continues forward and is joined by a larger, crimson hall running North.","The hall ends here, with a portrait that looks much like you. If you knew what you looked like."],[None,"You are at the northwest section of the pillar. passageways branch north, south, and east.","You are at the northeast section of the pillar. You feel a warm breeze move through the cave here, soothing you.\nPathways lead North,South,and West from here.",None,"The hall becomes a truer hue of crimson, and ornate gold lones paint the ceiling above you."],["""You have found the Cartographer's Room!
          O         T
          |         |
     O----O----O    O
     |    |    |    |
O----O    R    O    O
     |    |    |    |
O----O    O----O    O
     |    |         |
     O----O         O
     |    |         |
O----O----O----O----O----O
          |    |
          X    O
This is painted on one of the walls.
    ""","The air around you smells of old sushi and stale Baleen Bits.\nPathways lead North, South, and West.","You can feel a warmth from the North. The path splits off here, going from a n/s hall to an eastward tunnel.","The tunnel grows dim and heads North and West.","You feel a chill go down your spine as you continue through the dim hallway."],["You are in a small room with a pedestal.","You are in a large antechamber filled halfway with water.","You are in the resting room. A small ever-burning fire warms the floor, which is covered with a soft, snow-white layer of grass.","The tunnel continues North and South.","You can see a large red door far ahead of you. The hall continues."],[None,"The pathway turns sharply. Paths are to the East and South.","There is a junction to the North here.","The air around you smells of something or other. The path from the West continues South as a rough cave.","You are at the bright red door."],[None,None,"Nothing here. Other than you, of course.",None,"You are in the dragon's den!"]]
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
