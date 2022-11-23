import re


def tokenize(code):
    rules = [
        ('BREAK', r'break'),        # break
        ('CONST', r'const'),        # const
        ('CASE', r'case'),          # case
        ('CATCH', r'catch'),        # catch
        ('CONTINUE', r'continue'),  # continue
        ('DEFAULT', r'default'),    # default
        ('DELETE', r'delete'),      # delete
        ('ELSE_IF', r'else if'),    # else if
        ('ELSE', r'else'),          # else
        ('FALSE', r'false'),        # false
        ('FINALLY', r'finally'),    # finally
        ('FOR', r'for'),            # for
        ('FUNCTION', r'function'),  # function
        ('IF', r'if'),              # if
        ('LET', r'let'),            # let
        ('NULL', r'null'),          # null
        ('RETURN', r'return'),      # return
        ('SWITCH', r'switch'),      # switch
        ('THROW', r'throw'),        # throw
        ('TRY', r'try'),            # try
        ('TRUE', r'true'),          # true
        ('VAR', r'var'),            # var
        ('WHILE', r'while'),        # while
        ('LBRACKET', r'\('),        # (
        ('RBRACKET', r'\)'),        # )
        ('LBRACE', r'\{'),          # {
        ('RBRACE', r'\}'),          # }
        ('COMMA', r','),            # ,
        ('DOT', r'\.'),             # .
        ('SEMI_COLON', r';'),       # ;
        ('COLON', r'\:'),           # :
        ('STRING', r'\"[^\"\n]*\"|\'[^\'\n]*\''),  # "string"
        ('DOUBLE_QUOTE', r'\"'),    # "
        ('EQ', r'=='),              # ==
        ('NE', r'!='),              # !=
        ('LE', r'<='),              # <=
        ('GE', r'>='),              # >=
        ('OR', r'\|\|'),            # ||
        ('AND', r'&&'),             # &&
        ('ATTR', r'\='),            # =
        ('LT', r'<'),               # <
        ('GT', r'>'),               # >
        ('PLUS', r'\+'),            # +
        ('MINUS', r'-'),            # -
        ('MULT', r'\*'),            # *
        ('COMMENT', r'\/\/[^\n]*|\/\*[^\*\/]*\*\/'), # // or /* */
        ('DIV', r'\/'),             # /
        ('VARIABLE', r'[a-zA-Z]\w*'),     # VARIABLE
        ('FLOAT', r'\d(\d)*\.\d(\d)*'),   # FLOAT
        ('INTEGER', r'\d(\d)*'),          # INT
        ('NEWLINE', r'\n'),         # NEW LINE
        ('SKIP', r'[ \t]+'),        # SPACE and TABS
        ('MISMATCH', r'.')         # ANOTHER CHARACTER
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
