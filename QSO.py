##############################################################################################
#                                       Import
##############################################################################################

from random import randint
from Character import Character
from Radix import KVEntry
from Radix import Sort
from PC import Player
from Gnoblin import Gnoblin
from Selection import Selection
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
        getInput()

def getInput():
    global gameState
    global player
    global quit
    options = [];
    if(gameState == "Load"):
        options.append(Selection("New Game", ["new", "new game"], "create()"))
        options.append(Selection("Load Game", ["load", "load game"], "load()"))
    if gameState == "Running":
        options.append(Selection("Fight", ["fight", "fight something"], "testCombat()"))
        options.append(Selection("Level Up", ["level", "level up"], "testLevel()"))
        options.append(Selection("Save Game", ["save", "save game"], "save()"))
    if gameState == "Combat":
        pass
    options.append(Selection("Exit Game", ["exit", "exit game"], "quitGame()"))
    stroptions = "("
    for i in range(0, len(options), 1):
        stroptions += str(options[i])
        if i < len(options)-1:
            stroptions += ", "
    stroptions += ")"
    valid = False
    selection = None
    while not valid:
        valInput = input("What would you like to do? " + str(stroptions) + "\n>").lower()
        for sel in options:
            if sel.validSel(valInput):
                valid = True
                selection = sel
                break
    exec(sel.codeToExecute)

def quitGame():
    global quit
    quit = True

def testLevel():
        player.AP = 100
        player.checkLevel()

def testCombat():
    global player
    entities = []
    entities.append(player)
    entities.append(Gnoblin(1))
    _combat(entities)

def create():
    global player
    global gameState
    player = Player()
    gameState = "Running"

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

def _combat(entities):
    global gameState
    global player
    for en in entities:
        print("PC", isinstance(en, Player))
        print("Gnoblin", isinstance(en, Gnoblin),type(en))
    sEntities = sortEntities(entities)
    for en in sEntities:
        print("PC", isinstance(en, Player))
        print("Gnoblin", isinstance(en, Gnoblin),type(en))
    for i in range(0, len(sEntities)):
        sEntities[i].hitSomething(sEntities)
    
def sortEntities(entities):
    orderedEntities = []
    orderedInitiative = []
    initiative = []
    neg = 0
    for i in range(0, len(entities)):
        initiative.append(entities[i].initiative())
        try:
            if int(initiative[i]) < neg:
                neg = initiative[i]
        except:
            pass
    for i in range(0, len(initiative)):
        initiative[i] = int(initiative[i]) + neg
    orderedInitiative = Sort(initiative)
    for i in range(0, len(orderedInitiative)):
        for j in range(0, len(initiative)):
            if orderedInitiative[i] == initiative[j]:
                orderedEntities.append(entities[j])
                del entities[j]
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
        print(player.name," has been slain!")
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
