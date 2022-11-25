startState="q1"
finalState="q2"
wrongState="q3"

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
symbol ="_$"

def isAllNumber(input):
    allNumber=True
    for c in input:
        if not c in number:
            allNumber=False
    return allNumber

def checkVarName(input):
    state=startState
    for c in input:
        if state==startState:
            if c in UPPERCASE or c in lowercase or c in symbol:
                state=finalState
            if c in number:
                state=wrongState
        if state==finalState:
            if not c in UPPERCASE and not c in lowercase and not c in number and not c in symbol:
                state=wrongState
    return state==finalState