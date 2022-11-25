import sys
from src.Lexer import tokenize
from src.CYK import parse

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        try:
            file = open(sys.argv[1], 'r')
            text = file.read()
            file.close()
        except:
            print("\nFile tidak dapat dibuka!\n")

        token = tokenize(text)
        if(token[0]==-1):
            print("Terdapat nama variabel yang tidak tepat: ")
            print(token[1])
        else:
            print('\nTokens: ', token)
            parse(token)
    else:
        print("\nArgumen kurang dari 2!\n")
