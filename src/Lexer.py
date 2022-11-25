import re
from src.FA import checkVarName
from src.FA import isAllNumber

def tokenize(code):
    rules = [
        ('break', r'break\b'),                # break
        ('const', r'const\b'),                # const
        ('case', r'case\b'),                  # case
        ('catch', r'catch\b'),                # catch
        ('continue', r'continue\b'),          # continue
        ('default', r'default\b'),            # default
        ('delete', r'delete\b'),              # delete
        ('do', r'do\b'),                      # do
        ('else', r'else\b'),                  # else
        ('false', r'false\b'),                # false
        ('finally', r'finally\b'),            # finally
        ('for', r'for\b'),                    # for
        ('function', r'function\b'),          # function
        ('if', r'if\b'),                      # if
        ('let', r'let\b'),                    # let
        ('new', r'new\b'),                    # new
        ('null', r'null\b'),                  # null
        ('return', r'return\b'),              # return
        ('switch', r'switch\b'),              # switch
        ('throw', r'throw\b'),                # throw
        ('try', r'try\b'),                    # try
        ('true', r'true\b'),                  # true
        ('var', r'var\b'),                    # var
        ('while', r'while\b'),                # while
        ('undefined', r'undefined\b'),        # undefined
        ('in', r'in\b'),                      # in
        ('openpar', r'\('),                 # (
        ('closepar', r'\)'),                # )
        ('openbrac', r'\{'),                # {
        ('closebrac', r'\}'),               # }
        ('arrayopen', r'\['),               # [
        ('arrayclose', r'\]'),              # ]
        ('question', r'\?'),                # ?
        ('comma', r','),                    # ,
        ('dot', r'\.'),                     # .
        ('semicolon', r';'),                # ;
        ('colon', r'\:'),                   # :
        ('string', r'\"[^\"\n]*\"|\'[^\'\n]*\''),  # "string"
        ('quote', r'\"'),                   # "
        ('aposthrope', r'\''),              # '
        ('funcline', r'\=\>'),              # =>
        ('strictcompare', r'==='),          # ===
        ('compare', r'=='),                 # ==
        ('strictnotcompare', r'!=='),       # !==
        ('notcompare', r'!='),              # !=
        ('smallerequalthan', r'<='),        # <=
        ('biggerequalthan', r'>='),         # >=
        ('logicandequal', r'\&\&\='),       # &&=
        ('logicorequal', r'\|\|\='),        # ||=
        ('logicor', r'\|\|'),               # ||
        ('logicand', r'&&'),                # &&
        ('plusequal', r'\+\='),             # +=
        ('minequal', r'\-\='),              # -=
        ('multequal', r'\*\='),             # *=
        ('divequal', r'\/\='),              # /=
        ('modequal', r'\%\='),              # %=
        ('powequal', r'\*\*\='),            # **=
        ('shiftleftequal', r'\<\<\='),      # <<=
        ('shiftarithrightequal', r'\>\>\='),    # >>=
        ('shiftlogicrightequal', r'\>\>\>\='),  # >>>=
        ('shiftleft', r'\<\<'),             # <<
        ('shiftlogicright', r'\>\>\>'),     # >>>
        ('shiftarithright', r'\>\>'),       # >>
        ('andequal', r'\&\='),              # &=
        ('xorequal', r'\^\='),              # ^=
        ('orequal', r'\|\='),               # |=
        ('equal', r'\='),                   # =
        ('smallerthan', r'<'),              # <
        ('biggerthan', r'>'),               # >
        ('increment', r'\+\+'),             # ++    
        ('decrement', r'\-\-'),             # --
        ('plus', r'\+'),                    # +
        ('minus', r'-'),                    # -
        ('power', r'\*\*'),                 # **
        ('mult', r'\*'),                    # *
        ('comment', r'\/\/[^\n]*|\/\*[^\*\/]*\*\/'),  # // or /* */
        ('divide', r'\/'),                  # /
        ('modulo', r'\%'),                  # %
        ('logicnot', r'\!'),                # !
        ('and', r'\&'),                     # &
        ('or', r'\|'),                      # |
        ('xor', r'\^'),                     # ^
        ('not', r'\~'),                     # ~
        ('variable', r'[a-zA-Z0-9\_\$][a-zA-Z0-9\_\$]*'),       # variable
        ('number', r'\d(\d)*'),             # number
        ('endline', r'\n'),                 # new line
        ('SKIP', r'[ \t]+'),                # space and tabs
        ('MISMATCH', r'.')                  # unknown?!!
    ]

    tokensJoin = '|'.join('(?P<%s>%s)' % x for x in rules)
    token = []
    wrongVarName=False
    theName=""
    for m in re.finditer(tokensJoin, code):
        tokenType = m.lastgroup
        tokenLexeme = m.group(tokenType)

        if tokenType == 'SKIP' or tokenType == 'comment' or tokenType == 'endline':
            continue
        elif tokenType == 'variable':
            if isAllNumber(tokenLexeme):
                token.append('number')
            elif(not checkVarName(tokenLexeme)):
                wrongVarName=True
                theName=tokenLexeme
                break
            else:
                token.append(tokenType)
        elif tokenType == 'MISMATCH':
            raise RuntimeError('%r unexpected token' % (tokenLexeme))
        else:
            token.append(tokenType)
    if wrongVarName:
        return [-1,theName]
    return token
