##############################################################################################
#                                       Import
##############################################################################################
from random import randint
from Character import Character
from PC import Player
from Gnoblin import Gnoblin
from Selection import Selection
from Combat import combat
import Globals
import sys
import pickle
import os
import Map
##############################################################################################
#                                       Variables
##############################################################################################

#Flag if a char has already been created

##############################################################################################
#                                       Functions
##############################################################################################
def _main():
    Globals.gameState = "Load"
    while not Globals.quitGame:
        getInput()

def getInput():
    options = [];
    if(Globals.gameState == "Load"):
        options.append(Selection("New Game", ["new", "new game"], "create()"))
        options.append(Selection("Load Game", ["load", "load game"], "load()"))
    if Globals.gameState == "Running":
        options.append(Selection("Fight", ["fight", "fight something"], "testCombat()"))
        if Globals.player.AP >= 100:
            options.append(Selection("Level Up", ["level", "level up"], "level()"))
        options.append(Selection("Save Game", ["save", "save game"], "save()"))
        options.append(Selection("Display Character",["display","display character"], "print(Globals.player)"))
    if Globals.gameState == "Dungeon":
        options.append(Selection("Move(N,S,E,W)",["n","north","s","south","e","east","w","west"],"Map.mapMain(valInput)"))
        if Globals.player.AP >= 100:
            options.append(Selection("Level Up", ["level", "level up"], "level()"))
        options.append(Selection("Save Game", ["save", "save game"], "save()"))
        if Map.positionCheck() == [2,4]:
            options.append(Selection("Rest",["rest"],"Globals.player.rest()"))
        options.append(Selection("Display Character",["display","display character"], "print(Globals.player)"))
    if Globals.gameState == "Combat":
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
    userIn = input("Would you like to save first?").lower()
    if "y" in userIn:
        save()
    Globals.quitGame = True

def level():
    Globals.player.checkLevel()

def testCombat():
    entities = []
    entities.append(Globals.player)
    entities.append(Gnoblin(1))
    combat(entities)

def create():
    Globals.player = Globals.player()
    Globals.gameState = "Dungeon"
    a,b = Map.positionCheck()
    Map.roomDesc(a,b)

def save():
    print("Saving...")
    if os.path.isfile("player.qso"):
        os.remove("player.qso")
    pickle.dump(Globals.player, open( "player.qso","wb"))
    print("Save complete!")

def load():
    print("Loading")
    if os.path.isfile("player.qso"):
        Globals.player = pickle.load( open( "player.qso","rb"))
        global loadingFlag
        loadingFlag = True
        Globals.gameState = "Dungeon"
        print(Globals.player.name,"loaded successfully.")
        a,b = Map.positionCheck()
        Map.roomDesc(a,b)
    else:
        print("Player not found")
for i in range(15):
    print(Gnoblin(i))
    
_main()
