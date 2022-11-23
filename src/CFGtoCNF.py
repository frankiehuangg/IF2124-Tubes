productions = []


def readFile(fileCFG):
    file = open(fileCFG, 'r')
    CFGProductions = file.readlines()
    for i in range(len(CFGProductions)):
        CFGProductions[i] = CFGProductions[i].replace('\n', '')
    for i in range(len(CFGProductions)):
        if(CFGProductions[i] == ''):
            continue
        if(CFGProductions[i][0] == '#'):
            continue
        LHS = CFGProductions[i].split(' -> ')[0]  # non-terminal
        # array of terminal/non-terminals
        RHS = CFGProductions[i].split(' -> ')[1].split(' | ')
        productions.append([LHS, RHS])


def writeFile():
    file = open("grammar/CNF.txt", 'w')
    for i in range(len(productions)):
        file.write(productions[i][0])
        file.write(' -> ')
        file.write(productions[i][1][0])
        for j in range(1, len(productions[i][1])):
            file.write(' | ' + productions[i][1][j])
        file.write('\n')


# Read file from 'CFG.txt'
readFile('grammar/CFG.txt')

# Step 1: Add S0 -> S, as S appears on the RHS
productions.insert(0, ['S0', ['S']])

# Step 2: Eliminate null (A -> ε), unit (A -> B), and useless productions
# Tidak mungkin ada null dan useless production, dihandle di CFG
# Eliminate Unit
loop = True
while (loop):
    loop = False
    for i in range(len(productions)):
        newRHS = []
        for j in range(len(productions[i][1])):
            if (productions[i][1][j].count(' ') == 0 and productions[i][1][j].isupper()):
                loop = True
                # Add RHS of non-terminal from index j (not symbol/lower-case)
                for k in range(len(productions)):
                    if (productions[k][0] == productions[i][1][j]):
                        newRHS += productions[k][1]
            else:
                newRHS.append(productions[i][1][j])
        productions[i][1] = newRHS

# Step 3: Eliminate terminals from RHS if exist with other terminals/ non-terminals (A -> aX)
# Tidak mungkin ada, dihandle di CFG

# Step 4: Eliminate non-terminals from RHS if exist more than 2 non-terminals (A -> ABC)
# Eliminate non-terminals > 2
ID = 1
loop = True
while (loop):
    loop = False
    for i in range(len(productions)):
        for j in range(len(productions[i][1])):
            if (productions[i][1][j].count(' ') >= 2):
                loop = True
                newVariable = ('AAA' + str(ID))
                ID += 1
                nonTerminals = productions[i][1][j].split(' ')
                productions.append([newVariable, nonTerminals[:2]])
                newRHS = newVariable
                for k in range(2, len(nonTerminals)):
                    newRHS += ' ' + nonTerminals[k]
                productions[i][1][j] = newRHS

# Write CNF to file 'CNF.txt'
writeFile()
