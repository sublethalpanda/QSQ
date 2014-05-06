from enum import Enum, unique
from random import randint

class Affix(Enum):

    @classmethod
    def getRandom(cls):
        return cls(randint(cls.getSmallest(), cls.getLargest()))

    @classmethod
    def getRandom(cls, min, max):
        validEnum = False
        enum = None
        while not validEnum:
            try:
                enum = cls(randint(min, max))
                validEnum = True
            except:
                pass
        return enum


    @classmethod
    def getSmallest(cls, floor):
        min = 0
        for en in cls:
            val = en.value
            if val < min and (floor == None or val > floor):
                min = val
        return cls(min)

    @classmethod
    def getMin(cls):
        return cls.getSmallest(None)

    @classmethod
    def getLargest(cls, ceil):
        max = 0;
        for en in cls:
            val = en.value
            if val > max and (ceil == None or val < ceil):
                max = val
        return cls(max)

    @classmethod
    def getMax(cls):
        return cls.getLargest(None)

    @classmethod
    def getSizeFor(cls, level):
        return cls.getRandom(level-cls.getMax().value, level+cls.getMin().value)

@unique
class Suffix(Affix):
    Gnoblin = 0
    Copter = 10
    Man = 3
    Troll = 4
    WhoMustNotBeNamed = 40
    Oakenshield = 14
    Drunk = -3
    Fart = -15
    Face = -12
    Arm = -29
    King = 12
    Haensel = 13

@unique
class Prefix(Affix):
    Gnoblin = 0
    Sad = -1
    Poor = -2
    Big = 1
    Dragon = 10
    Man = 3
    Pirate = 4
    Pointy = 5
    CakeSlaying = 6
    Haggardly = 7
    PotatoFaced = 8
    TreeSkin = 9
    Shieldless = 11
    Obama = 12
    HulkBeef = 13
    Sightless = 14
    ManHater = 15
    LadyLicker = 16
    PizzaPicker = 17
    FatAss = 18
    Rapping = 19
    SurfHippie = 20
    Norwegian = 21
    Candy = 22
    Gamer = 250
    OakenShieldless = 50
    Unicorn = 23
    Pegaus = 100
    Budski= 150
    Skinner = 111
    Angushied = -4
    Armless = -50
    Legless = -60
    Headless = -100
    Heartless = 500
    Cursed = -231
    Ginger = -9000
    CuteAnimeGirl = -1000
    Puppy = -5
    Drunkin = -12
    DunkinDonuts = -13
    DrunkenMaster = 2000
    Over9000 = 9001
    Smallest = -3
    BatmanCosplay = -58
    FireLord = 15000
    CreppyLittleChild = -1001
    DonkeyKong = 51
    CheesyJokes = -17
    Riddler = -90
    Haensel = 24
    Michael = 25

def get(level):
    valid = False
    prefix = None
    suffix = None
    while not valid:
        prefix = Prefix.getRandom(Suffix.getMin().value + level, Suffix.getMax().value - level)
        try:
            suffix = Suffix(level-prefix.value)
            if prefix.value + suffix.value == level:
                valid = True
        except:
            pass
    return {'prefix':prefix,'suffix':suffix}

def getGnoblinName(level):
    g = get(level)
    return g['prefix'].name + " Gnoblin " + g['suffix'].name

#
# ##
# ##Table I
# ##Dice: Result
# ##01-06 Accursed
# ##07-12 Ancient
# ##13-14 Baneful
# ##15-18 Batrachian
# ##19-25 Black
# ##26-28 Bloodstained
# ##29-30 Cold
# ##31-38 Dark
# ##39-40 Devouring
# ##41-42 Diabolical
# ##43-44 Ebon
# ##45-47 Eldritch
# ##48-51 Forbidden
# ##52-55 Forgotten
# ##56-57 Haunted
# ##58-61 Hidden
# ##62-63 Lonely
# ##64-67 Lost
# ##68-69 Malevolent
# ##70-71 Misplaced
# ##72-73 Nameless
# ##74-75 Ophidian
# ##76-77 Scarlet
# ##78-80 Secret
# ##81-82 Shrouded
# ##83-84 Squamous
# ##85-86 Strange
# ##87-88 Tenebrous
# ##89-90 Uncanny
# ##91-92 Unspeakable
# ##93-94 Unvanquishable
# ##95-96 Unwholesome
# ##97-98 Vanishing
# ##99-00 Weird
# ##
# ##
# ##Table II
# ##Dice: Result
# ##01-02 Abyss
# ##03-05 Catacombs
# ##06-10 Caverns
# ##11-13 Citadel
# ##14-15 City
# ##16-17 Cyst
# ##18-21 Depths
# ##22-26 Dungeons
# ##27-30 Fane
##31-33 Fortress
##34-36 Halls
##37-38 Haunts
##39-40 Isle
##41-43 Keep
##44-49 Labyrinth
##50-53 Manse
##54-60 Maze
##61-62 Milieu
##63-67 Mines
##68-71 Mountain
##72-74 Oubliette
##75-77 Panopticon
##78-81 Pits
##82-84 Ruins
##85-87 Sanctum
##88-89 Shambles
##90-93 Temple
##94-95 Tower
##96-00 Vault
##
##Table III
##Dice: Result
##01-00 of
##
##Table IV
##Dice: Result
##01-02 the Axolotl
##03-04 Blood
##05-06 Bones
##07-08 Chaos
##09-11 the (Table I) Cult
##12-13 Curses
##14-15 the Dead
##16-17 Death
##18-19 Demons
##20-21 Despair
##22-23 Deviltry
##24-25 Doom
##26-27 the Dweller(s) in [01-50] the (Table II) [51-00] (Table IV)
##28-29 (Table I) Dweomercraeft
##30-31 Evil
##32-33 Fire
##34-35 Frost
##36-37 the (3-13) Geases
##38-39 Gloom
##40-41 Hells
##42-43 Horrors
##44-45 Ichor
##46-47 Id Insinuation
##48-49 the (Table I) Idol
##50-51 Iron
##52-53 Madness
##54-55 Mirrors
##56-57 Mists
##58-59 Monsters
##60-61 Mystery
##62-63 Necromancy
##64-65 Oblivion
##66-68 the (Table I) One(s)
##69-70 Peril
##71-72 Phantasms
##73-74 Random Harlots
##75-76 Secrets
##77-78 Shadows
##79-80 Sigils
##81-82 Skulls
##83-84 Slaughter
##85-86 Sorcery
##87-88 Syzygy
##89-90 Terror
##91-92 Torment
##93-94 Treasure
##95-96 the Undercity
##97-98 the Underworld
##99-00 the Unknown
##100-101 Liam Neesons
##102-103 Articuno

##
##http://www.basicfantasy.org/dungeoneer.html
##