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
    Arm = -29
    Fart = -15
    Face = -12
    Hobo=-6
    Drunk = -3
    Programmer = -2
    Teddy = -1
    Gnoblin = 0
    Fish = 1
    Turtle = 2
    Man = 3
    Troll = 4
    Senior = 5
    Hippo = 6
    Teacup =7
    Monster = 8
    Chair = 9
    Copter = 10
    Thwopter = 11
    King = 12
    Haensel = 13
    Oakenshield = 14
    ThwopterCopter = 15
    Breaker = 16
    Here = 17
    Elf=27
    WhoMustNotBeNamed = 40
    Devil=50
    Gnoblinoid = 60
    Dragon = 70
    Abyss = 100
    Catacombs = 101
    Caverns = 102
    Citadel = 103
    City = 104
    Cyst = 105
    Depths = 106
    Dungeons = 107
    Fane = 108
    Fortress = 109
    Halls = 110
    Haunts = 111
    Isle = 112
    Keep = 113
    Labyrinth = 114
    Manse = 115
    Maze = 116
    Milieu = 117
    Mines = 118
    Mountain = 119
    Oubliette = 120
    Panopticon = 121
    Pits = 122
    Ruins = 123
    Sanctum = 124
    Shambles = 125
    Temple = 126
    Tower = 127
    Vault = 128

@unique
class Prefix(Affix):
    Ginger = -9000
    CreppyLittleChild = -1001
    CuteAnimeGirl = -1000
    Cursed = -231
    Headless = -100
    Riddler = -90
    Legless = -60
    BatmanCosplay = -58
    Armless = -50
    Lonely = -21
    Lost = -20
    CheesyJokes = -17
    Insert = -16
    DunkinDonuts = -13
    Drunkin = -12
    Weird = -8
    Sightless = -7
    Puppy = -5
    Angushied = -4
    Smallest = -3
    Poor = -2
    Sad = -1
    Gnoblin = 0
    Big = 1
    Man = 3
    Pirate = 4
    Pointy = 5
    CakeSlaying = 6
    Haggardly = 7
    PotatoFaced = 8
    TreeSkin = 9
    Dragon = 10
    Shieldless = 11
    Obama = 12
    HulkBeef = 13
    Aggressive = 14
    ManHater = 15
    LadyLicker = 16
    PizzaPicker = 17
    FatAss = 18
    Rapping = 19
    SurfHippie = 20
    Norwegian = 21
    Candy = 22
    Unicorn = 23
    Haensel = 24
    Michael = 25
    PurplePeoplEater=26
    FireNation = 27
    WaterBending = 28
    Accursed = 29
    Ancient = 30
    Baneful = 31
    Batrachian = 32
    Black = 33
    Bloodstained = 34
    Cold = 35
    Dark = 36
    Devouring = 37
    Diabolical = 38
    Ebon = 39
    Eldritch = 40
    Forbidden = 41
    Forgotten = 42
    Haunted = 43
    Hidden = 44
    Malevolent = 45
    Misplaced = 46
    Nameless = 47
    Ophidian = 48
    Scarlet = 49
    OakenShieldless = 50
    DonkeyKong = 51
    Secret = 52
    Shrouded = 53
    Squamous = 54
    Strange = 55
    Tenebrous = 56
    Uncanny = 57
    Unspeakable = 58
    Unvanquishable = 59
    Unwholesome = 60
    Vanishing = 61
    LiamNeesons = 62
    Articuno = 63
    Pegaus = 100
    Skinner = 111
    RainbowRiding=117
    Gamer = 250
    Budski = 150
    Heartless = 500
    DrunkenMaster = 2000
    Over9000 = 9001
    FireLord = 15000

def get(level):
    valid = False
    prefix = None
    suffix = None
    count = 0
    while not valid:
        prefix = Prefix.getRandom(Suffix.getMin().value + level, Suffix.getMax().value + level)
        try:
            suffix = Suffix(level-prefix.value)
            if prefix.value + suffix.value == level:
                valid = True
        except:
            pass
        count += 1
        if count == 1000000:
            print("We've gone through the loop 1 million times. I would recommend force quitting")
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
# ##DONE_______________
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




#The Axolotl
##03-04 Blood
##05-06 Bones
##07-08 Chaos
##12-13 Curses
##14-15 the Dead
##16-17 Death
##18-19 Demons
##20-21 Despair
##22-23 Deviltry
##24-25 Doom
##30-31 Evil
##32-33 Fire
##34-35 Frost
##38-39 Gloom
##40-41 Hells
##42-43 Horrors
##44-45 Ichor
##46-47 Id Insinuation
##50-51 Iron
##52-53 Madness
##54-55 Mirrors
##56-57 Mists
##58-59 Monsters
##60-61 Mystery
##62-63 Necromancy
##64-65 Oblivion
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
##95-96 The Undercity
##97-98 The Underworld
##99-00 The Unknown
