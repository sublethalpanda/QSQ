##############################################################################################
#                                       Import
##############################################################################################

from random import randint
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
        options.append("new game")
        options.append("load game")
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
    if usrin == "new game":
        charCreate(False)
    elif usrin == "load game":
        load()
    elif usrin == "save game":
        save()
    elif usrin == "level":
        player.AP = 100
        player.checkLevel()
    elif usrin == "fight":
        entities = []
        entities.append(player)
        entities.append(createEnemy(1))
        _combat(entities)
    elif usrin == "exit":
        quit = True

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

#-----------------------------Character Creation

def charCreate(loadingFlag):
    global gameState
    nameFlag = False
    while nameFlag == False:
        name = input("What should I call you?\n>")
        if len(name) > 15:
            print("That's quite a mouthful. Try shortening it.")
        else:
            nameFlag = True

    genderFlag = False
    while genderFlag == False:
        gender = input("Gender: Are you Male(M) or Female(F)?\n>").upper()
        gender = gender [0:1]
        if gender == "M" or gender == "F":
            genderFlag = True
        else:
            print("Please choose 'M' or 'F'.")

    raceFlag = False
    while raceFlag == False:
        race = "Human"
        print("You are a",race)
        raceFlag = True

    rollFlag = False
    rerollFlag = False
    rerolled = False
    while rollFlag == False:
        rolls = [randint(1,8)-randint(1,6),randint(1,8)-randint(1,6),randint(1,8)-randint(1,6)]
        LCK = randint(1,8)-randint(1,6)
        if sum(rolls) < 0:
            continue
        else:
            attributes = ["Strength", "Dexterity", "Mind"]
            statsChosen = [0,0,0]
            print("There are three stats: " + attributes[0] + ", " + attributes[1] + ", and " + attributes[2] + ".")
            for i in range(0, len(attributes)-1, 1):
                flag = False
                rerollFlag = False
                while flag == False:
                    print("Your rolls are as follows: ", end="")
                    for j in range(0, len(rolls)-1, 1):
                        print(str(rolls[j]) + ", ", end="")
                    if len(rolls) != 1:
                        print("and ", end="")
                    print(rolls[len(rolls)-1])
                    statChoiceString = "Which stat would you like to assign to " + attributes[i] + "?"
                    if rerolled == False:
                        statChoiceString = statChoiceString + "\nPress 'r' to reroll your stats.(This can be done only once!)\n>"
                    else:
                        statChoiceString = statChoiceString + "\n>"
                    statChoice = input(statChoiceString)
                    if "r" in statChoice and rerolled == False:
                        rerollFlag = True
                        break
                    else:
                        rerollFlag = False
                    try:
                        statChoice = int(statChoice)
                    except:
                        print("Try again.")
                        continue
                    if statChoice in rolls:
                        rolls.remove(statChoice)
                        statsChosen[i] = statChoice
                        flag = True
                    else:
                        print("That's not one of your stats!")
                if rerollFlag == True and rerolled == False:
                    break
            if rerollFlag == True and rerolled == False:
                rerolled = True
                continue
            statsChosen[2] = rolls[0]
            rolls = None
            rollFlag = True
    age = [0,30+randint(1,20)+randint(1,20)+randint(1,20)+randint(1,20)]
    ageFlag = False
    while ageFlag ==False:
        age[0] = input("Your maximum age is "+str(age[1])+". How old are you currently?\n>")
        try:
            age[0] = int(age[0])
            if age[0]>age[1]:
                print("You would have died of old age!")
            elif age[0] < 0:
                print("I'm not entirely sure you understand how age works.")
            elif age[0] < 8:
                print("I'm not giving a sword to a child.\nWell, I'm not giving you a sword anyways, but you get the point.")
            else:
                ageFlag = True
        except:
            print("An integer, please!")
    #name already set
    STR = statsChosen[0]
    DEX = statsChosen[1]
    MND = statsChosen[2]
    #LCK already set
    #inv type, weap type, name, damage die, to-hit
    weapon = ["weapon","melee","Unarmed",6,0]
    #inv type, name, AS, RR, RT, Max Dex
    armor = ["armor","Unarmored",0,0,0,None]
    inventory = []
    #Create an HP function here.
    #Temp,Max,Die,Rolls,Bonus
    hp = [0,0,0,0,0]
    hp[2] = 6
    hp[1] = randint(1,hp[2])+STR
    hp[0] = hp[1]
    hp[3] = 1
    level = 1
    ap = 0
    description = input("How would you describe your character?\n>")
    #Base attack stat: Default STR
    BAS = "STR"
    #Base defense stat: Default DEX
    BDS = "DEX"
    dodge = DEX+armor[2]
    if MND >=5:
        mpTemp = randint(1,4)+MND
        #Temp,Max,Die,Rolls,Bonus
        mp = [mpTemp,mpTemp,4,1,0]
        ppTemp = randint(1,4)+MND
        pp = [ppTemp,ppTemp,4,1,0]
        manaEnabled = True
    else:
        mp = [0,0,0,0,0]
        pp = [0,0,0,0,0]
        manaEnabled = False
    global player
    player = Character(name,STR,DEX,MND,LCK,weapon, armor, inventory, hp, level, ap, description, age, mp, pp, manaEnabled)
    print("A hero has risen!")
    gameState = "Running"
    print(gameState)

def createEnemy(level):
    name = "Gnoblin"
    statsFlag = False
    while statsFlag == False:
        STR = randint(1,8)-randint(1,6)
        DEX = randint(1,8)-randint(1,6)
        MND = randint(1,8)-randint(1,6)
        LCK = randint(1,8)-randint(1,6)
        if STR+DEX+MND >= 0:
            statsFlag = True
    armor = ["armor","Unarmored",0,0,0,None]
    weapon = ["weapon","melee","Unarmed",6,0]
    inventory = []
    hp = [0,0,0,0,0]
    hp[2] = 6
    hp[1] = randint(1,hp[2])+STR
    hp[0] = hp[1]
    hp[3] = 1
    ap = level*100 + (randint(0,99))
    description = "A depressingly small gnoblinoid."
    age = [randint(8,19),19+randint(1,30)]
    if MND >=5:
        manaEnabled = True
        mpTemp = randint(1,4)+MND
        mp = [mpTemp,mpTemp,4,1,0]
        ppTemp = randint(1,4)+MND
        pp = [ppTemp,ppTemp,4,1,0]
    else:
        manaEnabled = False
        mp = [0,0,0,0,0]
        pp = [0,0,0,0,0]
    #Create the foe.
    global foe
    foe = Character(name,STR,DEX,MND,LCK,weapon, armor, inventory, hp, level, ap, description, age, mp, pp, manaEnabled)


    #Stat Assignment
    for i in range(level):
        levelSelect = randint(1,5)
        foe.levelUp(levelSelect)
    return foe

def _combat(entities):
    sEntities = sortEntities(entities)
    for i in range(0, len(sEntities)):
        #sEntities[i].hitSomething(sEntities)
        pass

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

def Sort(array):
    return RadixSortAux(array, 1)
def RadixSortAux(array, digit):
    Empty = True
    digits = [KVEntry()]*len(array)
    SortedArray = [int]*len(array)
    for i in range(0, len(array)):
        digits[i] = KVEntry()
        digits[i].key = i
        print(str((array[i]/digit) % 10) + "LOOK!!!")
        digits[i].value = (array[i]/digit) % 10
        if array[i] / digit != 0:
            Empty = False
    if Empty:
        return array

    SortedDigits = CountingSort(digits)
    for i in range(0, len(SortedArray)):
        SortedArray[i] = array[SortedDigits[i].key]
    return RadixSortAux(SortedArray, digit * 10)

def CountingSort(ArrayA):
    ArrayB = [int]*(MaxValue(ArrayA) + 1)
    ArrayC = [KVEntry()]*len(ArrayA)

    for i in range(0, len(ArrayB)):
        ArrayB[i] = 0

    for i in range(0, len(ArrayA)):
        ArrayB[ArrayA[i].value] += 1

    for i in range(1, len(ArrayB)):
        ArrayB[i] += ArrayB[i - 1]

    for i in range(len(ArrayA)-1, -1, -1):
        value = ArrayA[i].value
        index = ArrayB[value]
        ArrayB[value] -= 1
        ArrayC[index-1] = KVEntry()
        ArrayC[index-1].key = i
        ArrayC[index-1].value = value

    return ArrayC

def MaxValue(arr):
    Max = arr[0].value
    for i in range(1, len(arr)):
        if arr[i].value > Max:
            Max = arr[i].value()
    return Max

def gameOver():
    print("Game over!")

##############################################################################################
#                                       Classes
##############################################################################################

#-----------------------------Character Class
class Character(object):
    name = ""
    STR = 0
    DEX = 0
    MND = 0
    LCK = 0
    weapon = []
    armor = []
    inventory = []
    description = ""
    age = 0
    BAS = ""
    BDS = ""
    HP = 0
    level = 0
    AP = 0
    MP = 0
    PP = 0
    manaEnabled = False
    def __init__(self,pName,pStr,pDex,pMnd,pLck,pWeapon, pArmor, pInventory, pHp, pLevel, pAp, pDescription, pAge, pMp, pPp, pManaEnabled):
        "An entity that can attack"
        self.name = pName
        self.STR = pStr
        self.DEX = pDex
        self.MND = pMnd
        self.LCK = pLck
        self.weapon = pWeapon
        self.armor = pArmor
        self.inventory = pInventory
        self.description = pDescription
        #Age,Lifespan
        self.age = pAge
        #Check attack stat with weapon type
        if self.weapon[1] == "melee":
            self.BAS = "STR"
        elif self.weapon[1] == "ranged":
            self.BAS = "DEX"
        elif self.weapon[1] == "magic":
            self.BAS = "MND"
        #Check defense stat with armor penalty
        self.BDS = "DEX"
        self.HP = pHp
        self.level = pLevel
        self.AP = pAp
        self.MP = pMp
        self.PP = pPp
        self.manaEnabled = pManaEnabled


    def summary(self):
        #Name and title
        print("\t\t"+self.name,"Level",self.level,"\n\t   Character Summary","\n\t\t Age:",self.age[0])
        #Health
        print("\tHP:",str(self.HP[0])+"/"+str(self.HP[1]))
        #Stats
        print("\tSTR:",self.STR,"\n\tDEX:",self.DEX,"\n\tMND",self.MND)
        if self.LCK>=5 or self.LCK <=-5:
            print("\tLCK:",self.LCK)
        #Magic and Psychic
        if self.manaEnabled == True:
            print("MP:",str(self.MP[0])+"/"+str(self.MP[1]))
            print("PP:",str(self.PP[0])+"/"+str(self.PP[1]))
        #Weapon and armor
        print("Equipped Weapon:",self.weapon[2],"\nEquipped Armor:",self.armor[1])
        print('"'+self.description+'"')

    def checkLevel(self):
        while player.AP >= 100:
            self.doLevel()

    def doLevel(self):
        levelFlag = False
        print("""What would you like to level up?
1.  STR
2.  DEX
3.  MND
4.  LCK
5.  HP Die
6.  Roll and add HP die to HP
7.  Mana Die
8.  Roll and add MP Die
9.  Psychic Die
10. Roll and add Psychic Die
11. Upgrade damage die for current weapon""")

        while not levelFlag:
            lvlIn = input("\n>").lower()
            options = ["str", "dex", "mnd", "lck", "hp die","roll hp","mp die","roll mp","pp die", "roll pp","damage"]
            results = ["STR increased!", "DEX increased!", "MND increased!",
                       "LCK increased!", "HP die increased"]
            try:
                lvlIn = int(lvlIn)
            except:
                lvlIn = options.index(lvlIn) + 1
            if lvlIn == 4 and (self.LCK >=5 or self.LCK <= -5):
                print("You don't have access to the LCK stat!")
            else:
                self.levelUp(lvlIn)
                print(results[lvlIn-1])
                self.level += 1
                levelFlag = True
                self.AP -= 100
                print("Player leveled up!")

    def levelUp(self,selection):
        #str, dex, mnd, lck, hpdie, roll hp,
        #unarmed dam, mpdie,roll mp,
        #ppdie, roll pp
        if selection == 1:
            self.STR += 1
            self.HP[1] += self.STR*self.HP[3]
        elif selection == 2:
            self.DEX += 1
        elif selection ==3:
            self.MND += 1
            if self.manaEnabled ==True:
                self.MP[1] += self.MND*self.MP[3]
                self.PP[1] += self.MND*self.PP[3]
        elif selection == 4:
            self.HP[2] += 4
        elif selection == 5:
            self.HP[1] += randint(1,self.HP[2])+self.STR
            self.HP[3] += 1
        elif selection == 6:
            self.MP[2] +=3
        elif selection == 7:
            self.MP[1] += randint(1,self.MP[2])+self.MND
        elif selection == 8:
            self.PP[2] +=3
        elif selection == 9:
            self.PP[1] += randint(1,self.PP[2])+self.MND
        elif selection == 10:
            self.weapon[3] += 4
            self.weapon[4] += 1

    def attack(self):
        if self.BAS == "STR":
            tempBonus = self.STR
        elif self.BAS == "DEX":
            tempBonus = self.DEX
        elif self.BAS == "MND":
            tempBonus = self.MND
        elif self.BAS == "LCK":
            tempBonus = self.LCK
        tempRoll = self.roll()

        if tempRoll != "crit" and tempRoll != "fumble":
            tempRoll += tempBonus + self.weapon[4]

        tempDamage = randint(1,self.weapon[3])+tempBonus
        return tempRoll,tempDamage

    def defend(self):
        if self.BDS == "STR":
            tempBonus = self.STR
        elif self.BDS == "DEX":
            tempBonus = self.DEX
        elif self.BDS == "MND":
            tempBonus = self.MND
        elif self.BDS == "LCK":
            tempBonus = self.LCK
        tempRoll = self.roll()
        if tempRoll != "crit" and tempRoll != "fumble":
            tempRoll += tempBonus + self.armor[2]
        return tempRoll

    def roll(self):
        tempRoll = randint(1,20)
        if tempRoll == 1:
            return "fumble"
        elif tempRoll == 20:
            return "crit"
        else:
            return tempRoll

    def die(self):
        apGain = int(foe.AP/player.level)
        player.AP += apGain
        print ("The",foe.name,"dies, giving you",apGain,"AP")

    def initiative(self):
        roll = self.roll()
        try:
            roll + self.DEX
        except:
            pass
        return roll
class KVEntry:
    _key = 0;
    _value = 0;

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if value >= 0:
            _key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        _value = value


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
