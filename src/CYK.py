productions = []


def readFile(fileCNF):
    file = open(fileCNF, 'r')
    CNFProductions = file.readlines()
    for i in range(len(CNFProductions)):
        CNFProductions[i] = CNFProductions[i].replace('\n', '')
    for i in range(len(CNFProductions)):
        if (CNFProductions[i] == ''):
            continue
        if (CNFProductions[i][0] == '#'):
            continue
        LHS = CNFProductions[i].split(' -> ')[0]  # non-terminal
        # array of terminal/non-terminals
        RHS = CNFProductions[i].split(' -> ')[1].split(' | ')
        productions.append([LHS, RHS])


readFile('grammar/CNF.txt')


def parse(token):
    tabel = [
            [[] for _ in range(len(token)-i)]
        for i in range(len(token))
    ]

    # isi tabel paling bawah
    for i in range(len(token)):
        for j in range(len(productions)):
            if token[i] in productions[j][1]:
                tabel[0][i].append(productions[j][0])

    # traversal dari tinggi 1 hingga teratas
    for i in range(1, len(token)):
        # j looping semua elemen pada ketinggian i
        for j in range(len(token)-i):

            for k in range(i):
                # coba semua kombinasi
                for l in range(len(tabel[k][j])):
                    for r in range(len(tabel[i-k-1][j+k+1])):
                        check = tabel[k][j][l] + " " + tabel[i-k-1][j+k+1][r]
                        for m in range(len(productions)):
                            if check in productions[m][1]:
                                if (productions[m][0] in tabel[i][j]):
                                    continue
                                tabel[i][j].append(productions[m][0])

    '''
    # print buat debug
    for n in range(len(token)):
        for i in range(len(token)-n):
            print(tabel[n][i])
        print('next')
    print('here')
    '''
    # mengeluarkan true jika S berada di kotak paling atas
    print('S' in tabel[len(token)-1][0])
    return 'S' in tabel[len(token)-1][0]
