##############################################################################################
#                                       Import
##############################################################################################

from random import randint
from Character import Character
from Radix import KVEntry
from Radix import Sort
from PC import Player
from Gnoblin import Gnoblin
import sys
import pickle
import os

##############################################################################################
#                                       Variables
##############################################################################################

#Flag if a char has already been created
loadingFlag = False
quit = False

##############################################################################################
#                                       Functions
##############################################################################################
def _main():
    global gameState
    global quit
    gameState = "Load"
    while not quit:
        doStuff(getInput())

def getInput():
    global gameState
    global player
    options = [];
    if(gameState == "Load"):
        options.append("new")
        options.append("load")
    if gameState == "Running":
        options.append("fight")
        options.append("level")
        options.append("save game")
    if gameState == "Combat":
        pass
    options.append("exit")
    stroptions = "("
    for i in range(0, len(options), 1):
        stroptions += options[i]
        if i < len(options)-1:
            stroptions += ", "
    stroptions += ")"
    valid = False
    while not valid:
        validateInput = input("What would you like to do? " + str(stroptions) + "\n>").lower()
        if validateInput in options:
            valid = True;
    doStuff(validateInput)

def doStuff(usrin):
    global quit
    while usrin == None:
        usrin = getInput()
    if "new" in usrin:
        create()
    elif "load" in usrin:
        load()
    elif "save" in usrin:
        save()
    elif usrin == "level":
        player.AP = 100
        player.checkLevel()
    elif usrin == "fight":
        entities = []
        entities.append(player)
        entities.append(Gnoblin(1))
        _combat(entities)
    elif usrin == "exit":
        quit = True

def create():
    global player
    player = Player()


def save():
    if os.path.isfile("player.qso"):
        os.remove("player.qso")
    global player
    pickle.dump(player, open( "player.qso","wb"))

def load():
    global gameState
    if os.path.isfile("player.qso"):
        global player
        player = pickle.load( open( "player.qso","rb"))
        global loadingFlag
        loadingFlag = True
        gameState = "Running"
    else:
        print("Player not found")

def main():
    newGame()
    while not update():
        print("doing something")
        return update()

def update():
    userIn = talk()
    #Check input here

def talk():
    userIn = input("\n>").lower()
    return userIn

def _combat(entities):
    global gameState
    gameState = "Combat"
    sEntities = sortEntities(entities)
    for i in range(0, len(sEntities)):
        #sEntities[i].hitSomething(sEntities)


def sortEntities(entities):
    orderedEntities = []
    orderedInitiative = []
    initiative = []
    neg = 0
    for i in range(0, len(entities)):
        initiative.append(entities[i].initiative())
        try:
            if int(initiative[i]) < neg:
                initiative[i] = neg
        except:
            pass
    for i in range(0, len(initiative)):
        initiative[i] = int(initiative[i]) + neg
    orderedInitiative = Sort(initiative)
    for i in range(0, len(orderedInitiative)):
        for j in range(0, len(initiative)):
            if orderedInitiative[i] == initiative[j]:
                orderedEntities.append(entities[j])
                break
    return orderedEntities

def combat():
    global combatFlag
    combatFlag = False
    while combatFlag == False:
        if player.DEX>foe.DEX:
            priority = 0
        elif player.DEX<foe.DEX:
            priority = 1
        else:
            priority = randint(0,1)
        if priority == 0:
            playerAtk()
            foeAtk()
        else:
            foeAtk()
            playerAtk()
    player.checkLevel()

def playerAtk():
    attackFlag = False
    while attackFlag == False:
        pHit, pDamage = player.attack()
        eDefend = foe.defend()
        selfDamage = 0
        try:
            pHit == int(pHit)
            eDefend == int(eDefend)
            if pHit < eDefend:
                pDamage = 0
        except:
            if pHit == "crit":
                if eDefend == "crit":
                    continue
                else:
                    pDamage = pDamage*2
            elif pHit == "fumble":
                selfDamage = randint(1,int(pDamage*2/3)+1)
                print(player.name,"fumbles, dealing",selfDamage,"to themselves!")
                pDamage = 0
        if eDefend == "fumble":
            pDamage=pDamage*2
        if pHit == "crit":
            print(player.name,"crits, dealing",pDamage,"to the",foe.name)
        elif pHit == "fumble":
            player.HP[0] = player.HP[0]-selfDamage
        elif pDamage == 0:
            print(player.name,"missed!")
        else:
            print(player.name,"hits, dealing",pDamage,"to the",foe.name)
        foe.HP[0] -= pDamage
        healthCheck()
        attackFlag = True

def foeAtk():
    attackFlag = False
    while attackFlag == False:
        eHit, eDamage = foe.attack()
        pDefend = player.defend()
        selfDamage = 0
        try:
            eHit = int(eHit)
            pDefend = int(pDefend)
            if eHit < pDefend:
                eDamage = 0
        except:
            if eHit == "crit":
                if pDefend == "crit":
                    continue
                else:
                    eDamage = eDamage*2
            elif eHit == "fumble":
                selfDamage = randint(1,int(eDamage*2/3)+1)
                print(foe.name,"fumbles, dealing",selfDamage,"to themself!")
                eDamage = 0
        if pDefend == "fumble":
            eDamage=eDamage*2
        if eHit == "crit":
            print("The",foe.name,"hits, dealing",eDamage,"to",player.name)
        elif eHit == "fumble":
            foe.HP[0] = foe.HP[0]-selfDamage
        elif eDamage == 0:
            print(foe.name,"missed!")
        else:
            print(foe.name,"hits, dealing",eDamage,"to the",player.name)
        player.HP[0] -= eDamage
        healthCheck()
        attackFlag = True

def healthCheck():
    if player.HP[0]<0:
        print(player.name,"has been slain!")
        global combatFlag
        combatFlag = True
        gameOver()
    elif foe.HP[0]<0:
        global combatFlag
        combatFlag = True
        foe.die()

def gameOver():
    print("Game over!")

##############################################################################################
#                                       Run
##############################################################################################

#if loadingFlag == False:
#    charCreate(loadingFlag)
#     loadingFlag = True
#     player.summary()
#     createEnemy(player.level)
#     foe.summary()
#     player.HP[0] = 9001
#     combat()
_main()
