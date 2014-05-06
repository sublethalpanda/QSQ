from random import randint
import sys

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


    def __str__(self):
        disp = ""
        #Name and title
        disp += "\t\t"+self.name,"Level",self.level,"\n\t   Character Summary","\n\t\t Age:",self.age[0]
        #Health
        disp +="\n"
        disp += "\tHP:",str(self.HP[0])+"/"+str(self.HP[1])
        #Stats
        disp += "\n"
        disp += "\tSTR:",self.STR,"\n\tDEX:",self.DEX,"\n\tMND",self.MND
        if self.LCK>=5 or self.LCK <=-5:
            disp += "\n"
            disp += "\tLCK:",self.LCK
        #Magic and Psychic
        if self.manaEnabled == True:
            disp += "\n"
            disp += "MP:",str(self.MP[0])+"/"+str(self.MP[1])
            disp += "\n"
            disp += "PP:",str(self.PP[0])+"/"+str(self.PP[1])
        #Weapon and armor
        disp += "\n"
        disp += "Equipped Weapon:",self.weapon[2],"\nEquipped Armor:",self.armor[1]
        disp += "\n"
        disp += '"'+self.description+'"'
        return disp

    def checkLevel(self):
        while self.AP >= 100:
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
                       "LCK increased!", "HP die increased!", "HP increased!",
                       "MP die increased!", "MP increased!", "PP die increased!",
                       "PP increased!", "Damage increased!"]
            try:
                lvlIn = int(lvlIn)
            except:
                lvlIn = options.index(lvlIn) + 1
            if lvlIn == 4 and (self.LCK <5 or self.LCK > -5):
                print("You don't have access to the LCK stat!")
            elif (lvlIn == 7 or lvlIn == 8) and self.manaEnabled == False:
                print("You don't have access to your MP abilities. Try increasing your MND.")
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

    def rolltoAttack(self):
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
        tempDamage = max(0, randint(1,self.weapon[3])+tempBonus)
        #print(tempDamage)
        return {'toHit':tempRoll,'damage':tempDamage}

    def rolltoDefend(self):
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
            tempRoll = -sys.maxsize-1
        elif tempRoll == 20:
            tempRoll = sys.maxsize
        return tempRoll

    def dead(self):
        return self.HP[0] < 0

    def die(self, killer):
        apGain = int(self.AP/killer.level)
        killer.AP += apGain
        print ("The",self.name,"dies, giving",killer.name,apGain,"AP")

    def initiative(self):
        roll = self.roll()
        try:
            roll + self.DEX
        except:
            pass
        return roll

    def attack(self, target):
        atRoll = self.rolltoAttack()
        defRoll = target.rolltoDefend()
        pdamage = 0
        if(atRoll['toHit'] > defRoll):
            pdamage = atRoll['damage']
            #RR and RT
            crfumble = ""
            if(atRoll['toHit'] > sys.maxsize / 2):
                crfumble = "Crits and"
                pdamage *= 2
            elif(atRoll['toHit'] < (-sys.maxsize-1) / 2):
                crfumbel = "Fumbles and"
                target = self
            target.damage(pdamage)
            print(self.name, crfumble, "Hits", target.name, "for", pdamage, "damage")
        else:
            print(self.name, "misses", target.name)
        if target.dead():
            target.die(self)

    def damage(self, pdamage):
#         print(self.HP, "      ", pdamage)
        self.HP[0] -= pdamage

    def hitSomething(self, target):
        print("super call")
