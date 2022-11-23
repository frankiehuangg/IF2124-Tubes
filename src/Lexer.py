import re


def tokenize(code):
    rules = [
        ('break', r'break'),                # break
        ('const', r'const'),                # const
        ('case', r'case'),                  # case
        ('catch', r'catch'),                # catch
        ('continue', r'continue'),          # continue
        ('default', r'default'),            # default
        ('delete', r'delete'),              # delete
        ('else', r'else'),                  # else
        ('false', r'false'),                # false
        ('finally', r'finally'),            # finally
        ('for', r'for'),                    # for
        ('function', r'function'),          # function
        ('if', r'if'),                      # if
        ('let', r'let'),                    # let
        ('null', r'null'),                  # null
        ('return', r'return'),              # return
        ('switch', r'switch'),              # switch
        ('throw', r'throw'),                # throw
        ('try', r'try'),                    # try
        ('true', r'true'),                  # true
        ('var', r'var'),                    # var
        ('while', r'while'),                # while
        ('undefined', r'undefined'),        # undefined
        ('in', r'in'),                      # in
        ('openpar', r'\('),                 # (
        ('closepar', r'\)'),                # )
        ('openbrac', r'\{'),                # {
        ('closebrac', r'\}'),               # }
        ('arrayopen', r'\['),               # [
        ('arrayclose', r'\]'),              # ]
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
        ('variable', r'[a-zA-Z]\w*'),       # variable
        ('number', r'\d(\d)*'),             # number
        ('endline', r'\n'),                 # new line
        ('SKIP', r'[ \t]+'),                # space and tabs
        ('MISMATCH', r'.')                  # unknown?!!
    ]

    tokensJoin = '|'.join('(?P<%s>%s)' % x for x in rules)
    token = []

    for m in re.finditer(tokensJoin, code):
        tokenType = m.lastgroup
        tokenLexeme = m.group(tokenType)

        if tokenType == 'SKIP':
            continue
        elif tokenType == 'MISMATCH':
            raise RuntimeError('%r unexpected token' % (tokenLexeme))
        else:
            token.append(tokenType)

    return token
