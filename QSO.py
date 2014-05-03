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
quitGame = False

##############################################################################################
#                                       Functions
##############################################################################################
def _main():
    global gameState
    global quitGame
    gameState = "Load"
    while not quitGame:
        getInput()

def getInput():
    global gameState
    global player
    global quitGame
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
    options.append(Selection("Exit Game", ["exit", "exit game"], "quitGameGame()"))
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

def quitGameGame():
    global quitGame
    quitGame = True

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
