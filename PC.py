from Character import Character
from random import randint

class Player(Character):
    def __init__(self, pName = None, pStr = None, pDex = None, pMnd = None, pLck = None, pWeapon = None, pArmor = None, pInventory = None, pHp = None,
                 pLevel = None, pAp = None, pDescription = None, pAge = None, pMp = None, pPp = None, pManaEnabled = None):
        if (pName == None and pStr == None and pDex == None and pMnd == None and pLck == None and
            pWeapon == None and pArmor == None and pInventory == None and pHp == None and pLevel == None and
             pAp == None and pDescription == None and pAge == None and pMp == None and pPp == None and pManaEnabled == None):
            self.charCreate();
        else:
            Character.__init__(self, pName, pStr, pDex, pMnd, pLck, pWeapon, pArmor, pInventory, pHp, pLevel, pAp, pDescription, pAge, pMp, pPp, pManaEnabled)

    def charCreate(self):
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
        Character.__init__(self, name,STR,DEX,MND,LCK,weapon, armor, inventory, hp, level, ap, description, age, mp, pp, manaEnabled)
        print("A hero has risen!")
        gameState = "Running"

    def hitSomething(self, entities):
        entities.remove(self)
        word = "are"
        if len(entities) == 1:
            word = "is"
        print("There", word, len(entities), "enemies;", end="")
        for enemy in entities:
            print("a level", enemy.level, enemy.name, end="")
        usrIn = input("\n What would you like to do? (Attack, Run Away)\n>").lower()
        if("run" in usrIn):
            return False
        elif("attack" in usrIn):
            validTarget = False
            selection = -1
            while not validTarget:
                print("Who would you like to attack?")
                for i in range(0, len(entities)):
                    print(i, "A level", entities[i].level, entities[i].name)
                usrIn = input(">")
                try:
                    selection = int(usrIn)
                    validTarget = True
                except:
                    pass

            self.attack(entities[i])