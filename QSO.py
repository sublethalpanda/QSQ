#Current bugs
#Selecting '1' for attacking a gnoblin results in target out of range.
#Selecting '0' results in attacking foe, not self.
#Not sure how the level up selection works, but I'm getting an out-of-index when attempting anything above or equal to 6.
#I can increase LCK without knowing it- meant to be mutable ONLY IF known.
#I'll bet I can increase MP as well, needs to depend on whether manaEnabled == True.

# Who would you like to attack?
# 0 A level 6 Mark
# 1 A level 1 Gnoblin
# >0
# Mark Hits Gnoblin for 8 damage
# Gnoblin Hits Gnoblin for 11 damage
# The Gnoblin dies, giving Gnoblin 173 AP
# What would you like to do? (Fight, Level Up, Save Game, Exit Game)



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
from Map import main

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
_main()
