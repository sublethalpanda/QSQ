from enum import Enum

class Affix(Enum):
    @classmethod
    def asdf(cls):
        pass

@Unique
class Suffix(Affix):
    Gnoblin = 0
    Copter = 10

@Unique
class Prefix(Affix):
    Gnoblin = 0
    Sad = -1
    Poor = -2
    Big = 1
    Dragon = 10