from Character import Character
from random import randint

class Gnoblin(Character):
    def __init__(self,level, pName = None, pStr = None, pDex = None, pMnd = None, pLck = None, pWeapon = None, pArmor = None, pInventory = None, pHp = None,
                 pLevel = None, pAp = None, pDescription = None, pAge = None, pMp = None, pPp = None, pManaEnabled = None):
        if (pName == None and pStr == None and pDex == None and pMnd == None and pLck == None and
            pWeapon == None and pArmor == None and pInventory == None and pHp == None and pLevel == None and
             pAp == None and pDescription == None and pAge == None and pMp == None and pPp == None and pManaEnabled == None):
            self.createEnemy(level)
        else:
            Character.__init__(self, pName, pStr, pDex, pMnd, pLck, pWeapon, pArmor, pInventory, pHp, pLevel, pAp, pDescription, pAge, pMp, pPp, pManaEnabled)
    def createEnemy(self, level):
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
        Character.__init__(self, name,STR,DEX,MND,LCK,weapon, armor, inventory, hp, level, ap, description, age, mp, pp, manaEnabled)
        #Stat Assignment
        for i in range(level):
            levelSelect = randint(1,5)
            self.levelUp(levelSelect)