from enum import Enum
from random import randint

class Affix(Enum):

    @classmethod
    def getRandom(cls):
        return cls(randint(cls.getSmallest(), cls.getLargest()))

    @classmethod
    def getRandom(cls, min, max):
        return cls(randint(min, max))

    @classmethod
    def getSmallest(cls, floor):
        min = 0
        for en in cls:
            if en < min and (ceil == None or en > ceil):
                min = en

    @classmethod
    def getSmallest(cls):
        cls.getSmallest(None)

    @classmethod
    def getLargest(cls, ceil):
        max = 0;
        for en in cls:
            if en > max and (ceil == None or en < ceil):
                max = en

    @classmethod
    def getLargest(cls):
        cls.getLargest(None)

@Unique
class Suffix(Affix):
    Gnoblin = 0
    Copter = 10
    Man = 3

@Unique
class Prefix(Affix):
    Gnoblin = 0
    Sad = -1
    Poor = -2
    Big = 1
    Dragon = 10
    Man = 3