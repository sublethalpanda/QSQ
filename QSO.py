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
#                                       Functions
##############################################################################################
def _main():
    Globals.gameState = "Load"
    while not Globals.quitGame:
        getInput()

def getInput():
    options = [];
    if Globals.gameState != "Load" and Globals.player.dead():
        Globals.quitGame = True
    else:
        if(Globals.gameState == "Load"):
            options.append(Selection("New Game", ["new", "new game"], "create()"))
            options.append(Selection("Load Game", ["load", "load game"], "load()"))

        if Globals.gameState == "Running":
            options.append(Selection("Fight", ["fight", "fight something"], "testCombat()"))
            options.append(Selection("Display Character",["display","display character"], "print(Globals.player)"))

        if Globals.gameState == "Dungeon":
            options.append(Selection("Move(N,S,E,W)",["n","north","s","south","e","east","w","west"],"Map.mapMain(valInput)"))
            if Map.positionCheck() == [0,4]:
                if Globals.getKey == False:
                    options.append(Selection("Get Key",["get","get key"],"Globals.getKey= True"))
            elif Map.positionCheck() == [4,5]:
                if Globals.doorUnlocked == False:
                    if Globals.getKey:
                        options.append(Selection("Unlock Door",["unlock","unlock door"],"Globals.doorUnlocked = True"))
            if Map.positionCheck() == [2,4]:
                options.append(Selection("Rest",["rest"],"Globals.player.rest()"))
            options.append(Selection("Display Character",["display","display character"], "print(Globals.player)"))
            if Globals.defeatBoss:
                options.append(Selection("New Game +",["new","new game", "new game +"],"newGamePlus()"))
            options.append(Selection("Cheat",["xyzzy"],"Globals.player.AP += 1000"))

        if Globals.gameState == "Combat":
            pass

        if Globals.gameState != "Load" and Globals.gameState != "Combat":
            if Globals.player.AP >= 100:
                options.append(Selection("Level Up", ["level", "level up"], "level()"))
            options.append(Selection("Save Game", ["save", "save game"], "save()"))
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
            valInput = input("\nWhat would you like to do? " + str(stroptions) + "\n>").lower()
            for sel in options:
                if sel.validSel(valInput):
                    valid = True
                    selection = sel
                    break
        exec(sel.codeToExecute)

def quitGame():
    userIn = input("Would you like to save first?\n>").lower()
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
    Globals.player = Player()
    Globals.gameState = "Dungeon"
    a,b = Map.positionCheck()
    Map.roomDesc(a,b)

def save():
    print("Saving...")
    if os.path.isfile("player.qso"):
        os.remove("player.qso")
    pickle.dump(Globals.player, open( "player.qso","wb"))
    print("Save complete!")
    if os.path.isfile("progress.qso"):
        os.remove("progress.qso")
    x,y = Map.positionCheck()
    globalsList = [Globals.doorUnlocked, Globals.miniBoss, Globals.defeatBoss, Globals.getKey,x,y,Globals.whaleTrap,Globals.levelInit]
    pickle.dump(globalsList, open( "progress.qso","wb"))

def load():
    print("Loading")
    if os.path.isfile("player.qso"):
        Globals.player = pickle.load( open( "player.qso","rb"))
        global loadingFlag
        loadingFlag = True
        Globals.gameState = "Dungeon"
        print(Globals.player.name,"loaded successfully.")
        a,b = Map.positionCheck()
        globalsList = pickle.load( open("progress.qso","rb"))
        Globals.doorUnlocked = globalsList[0]
        Globals.miniBoss = globalsList[1]
        Globals.defeatBoss = globalsList[2]
        Globals.getKey = globalsList[3]
        Map.position = [globalsList[4],globalsList[5]]
        Map.roomDesc(globalsList[4],globalsList[5])
        Globals.whaleTrap = globalsList[6]
        Globals.levelInit = globalsList[7]
    else:
        print("Player not found")
def newGamePlus():
    Globals.whaleTrap = False
    Globals.miniBoss = False
    Globals.defeatBoss = False
    Globals.doorUnlocked = False
    Globals.gameState = False
    Globals.quitGame = False
    Globals.getKey = False
    Globals.levelInit = Globals.player.level
    Map.position = [2,1]
    Map.roomDesc[Map.position[0],Map.position[1]]
    print("\nNew game started!\n")
_main()
