##############################################################################################
#                                       Import
##############################################################################################
from random import randint
from Character import Character
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
        options.append(Selection("Level Up", ["level", "level up"], "level()"))
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

def level():
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
    print("Saving...")
    if os.path.isfile("player.qso"):
        os.remove("player.qso")
    global player
    pickle.dump(player, open( "player.qso","wb"))
    print("Save complete!")

def load():
    global gameState
    print("Loading")
    if os.path.isfile("player.qso"):
        global player
        player = pickle.load( open( "player.qso","rb"))
        global loadingFlag
        loadingFlag = True
        gameState = "Running"
        print(player.name,"loaded successfully.")
    else:
        print("Player not found")

def _combat(entities):
    global gameState
    global player
    global quitGame
    sEntities = sortEntities(entities)
    combat = True
    while combat:
        for i in range(0, len(sEntities)):
            sEntities[i].hitSomething(sEntities[:])
        for en in sEntities:
            if en.dead():
                sEntities.remove(en)
        if player not in sEntities or len(sEntities) <= 1:
            combat = False
    if player.dead():
        print("You have been slain!")
        quitGame = True

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
    orderedInitiative = sorted(initiative)
    for i in range(len(orderedInitiative)-1, -1, -1):
        for j in range(len(initiative)-1, -1, -1):
            if orderedInitiative[i] == initiative[j]:
                orderedEntities.append(entities[j])
                break
    return orderedEntities
_main()
