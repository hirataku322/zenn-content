from enum import Enum


# class syntax
class Dog(Enum):
    SHIBAINU = 1, "s"
    POMERANIAN = 2, "p"
    SAMOYED = 3, "s"


class MyIntEnum(int, Enum):
    TWENTYSIX = "1a", 16


# Dog = Enum("Dog", [("SHIBAINU", 1), ("POMERANIAN", 2), ("SAMOYED", 3)])

print(MyIntEnum.TWENTYSIX.value)
