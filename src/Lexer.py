import re


def tokenize(code):
    rules = [
        ('BREAK', r'break'),            # break
        ('ASSIGN_CONST', r'const'),     # const
        ('SWITCH_CASE', r'case'),       # case
        ('CATCH_CATCH', r'catch'),      # catch
        ('CONTINUE', r'continue'),      # continue
        ('SWITCH_DEFAULT', r'default'), # default
        ('DELETE', r'delete'),          # delete
        #('ELSE_IF', r'else if'),       # else if
        ('COND_ELSE', r'else'),         # else
        ('FALSE', r'false'),            # false
        ('CATCH_FINALLY', r'finally'),  # finally
        ('LOOP_FOR', r'for'),           # for
        ('FUNC_FUNCTION', r'function'), # function
        ('COND_IF', r'if'),             # if
        ('ASSIGN_LET', r'let'),         # let
        ('NULL', r'null'),              # null
        ('FUNC_RETURN', r'return'),     # return
        ('SWITCH_SWITCH', r'switch'),   # switch
        ('CATCH_THROW', r'throw'),      # throw
        ('CATCH_TRY', r'try'),          # try
        ('TRUE', r'true'),              # true
        ('ASSIGN_VAR', r'var'),         # var
        ('LOOP_WHILE', r'while'),       # while
        ('OPENPAR', r'\('),             # (
        ('CLOSEPAR', r'\)'),            # )
        ('OPENBRAC', r'\{'),            # {
        ('CLOSEBRAC', r'\}'),           # }
        ('COMMA', r','),                # ,
        ('DOT', r'\.'),                 # .
        ('SEMICOLON', r';'),            # ;
        ('COLON', r'\:'),               # :
        ('STRING', r'\"[^\"\n]*\"|\'[^\'\n]*\''),  # "string"
        ('QUOTE', r'\"'),               # "
        ('COMPARE', r'=='),             # ==
        ('NOTCOMPARE', r'!='),          # !=
        ('SMALLEREQUALTHAN', r'<='),    # <=
        ('BIGGEREQUALTHAN', r'>='),     # >=
        ('LOGICOR', r'\|\|'),           # ||
        ('LOGICAND', r'&&'),            # &&
        ('EQUAL', r'\='),               # =
        ('SMALLERTHAN', r'<'),          # <
        ('BIGGERTHAN', r'>'),           # >
        ('PLUS', r'\+'),                # +
        ('MINUS', r'-'),                # -
        ('MULT', r'\*'),                # *
        ('COMMENT', r'\/\/[^\n]*|\/\*[^\*\/]*\*\/'), # // or /* */
        ('DIVIDE', r'\/'),              # /
        ('TEXT', r'[a-zA-Z]\w*'),       # VARIABLE
        #('FLOAT', r'\d(\d)*\.\d(\d)*'),# FLOAT
        ('NUMBER', r'\d(\d)*'),         # INT
        ('ENDLINE', r'\n'),             # NEW LINE
        ('SKIP', r'[ \t]+'),            # SPACE and TABS
        ('MISMATCH', r'.')              # ANOTHER CHARACTER
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
