import enum


class TokenKind(enum.Enum):
    end = 0,
    identifier = 1,
    string = 2
    num = 3
    arithmetic = 4
    logical = 5
    assignment = 6
    controlflow = 7
    brackets = 8
    input = 9


