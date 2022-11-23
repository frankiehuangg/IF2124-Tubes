def updateToCNF(CFG : dict):
    newProduction = {}
    for var in CFG:
        terminals = []
        productions = CFG[var]
        # Mencari terminal
        processProduction = [production for production in productions if len(production) > 1]
        for production in processProduction:
            for item in production:
                if not(isVariable(item)) and item not in terminals:
                    terminals.append(item)
        # Membuat produksi baru
        for i, terminal in enumerate(terminals):
            newProduction.update({f"{var}_TERM_{i + 1}": [[terminal]]})
            for idx, j in enumerate(productions):
                if len(j) > 1:
                    for k in range(len(j)):
                        if len(productions[idx][k]) == len(terminal):
                            productions[idx][k] = productions[idx][k].replace(terminal, f"{var}_TERM_{i + 1}")
        # Mengubah produksi sehingga hanya ada A -> BC atau A -> terminal
        idx = 1
        for i in range(len(productions)):
            while len(productions[i]) > 2:
                newProduction.update({f"{var}_{idx}": [[productions[i][0], productions[i][1]]]})
                productions[i] = productions[i][1:]
                productions[i][0] = f"{var}_{idx}"
                idx += 1
    CFG.update(newProduction)
    return CFG

import numpy as np

def CYK(w: str, lang: dict):
    w = w + "\n"
    n = len(w) 
    m = len(lang)
    dp = np.zeros((n+1, n+1, m+1))
    id = dict(zip(lang, [i for i in range(1, m+1)]))
    rule = [None]
    for var in lang:
        rule.append(lang[var])

    for i in range(1,n+1):
        for j in range(1,m+1):
            for term in rule[j]:
                # print(term)
                if(term[0]=='__or__'):
                    tmp = '|'
                elif(term[0]=='__nl__'):
                    tmp = '\n'
                else:
                    tmp = term[0]
                if(tmp==w[i-1]):
                    dp[1][i][j] = True
                    break
                
    for l in range(2, n+1):
        for s in range(1, n-l+2):
            for p in range(1, l):
                for i in range(1, m+1):
                    for term in rule[i]:
                        if(len(term)!=1):
                            j = id[term[0]]
                            k = id[term[1]]
                            if(dp[p][s][j] and dp[l-p][s+p][k]):
                                dp[l][s][i] = True
                                break
                                
    if(dp[n][1][1]):
        return -1
    else:
        lines = w.split('\n')
        idLines = dict(zip([i for i in range(len(w)) if w[i]=='\n'], [i for i in range(len(lines))]))
        ret = 1
        for i in range(n, 0, -1):
            if(dp[i][1][1]):
                break
            if(w[i-1]=='\n'):
                ret = idLines[i-1]
        return ret



