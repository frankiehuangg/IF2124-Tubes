import sys
from src.Lexer import tokenize


if __name__ == '__main__':

    if (len(sys.argv) > 1):
        try:
            file = open(sys.argv[1], 'r')
            text = file.read()
            file.close()
        except:
            print("\nFile tidak dapat dibuka!\n")

        token = tokenize(text)

        print('\nTokens: ', token)
    else:
        print("\nArgumen kurang dari 2!\n")
