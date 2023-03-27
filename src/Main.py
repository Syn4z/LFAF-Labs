from src.lexer.Lexer import Lexer
from src.lexer.Token import Token

if __name__ == '__main__':

    input_string = 'x = 3 + 4 * 2; y = x - 5;'
    tokensE = Token.tokens

    lexer = Lexer(input_string, tokensE)
    tokens = lexer.lex()

    print("First segment: \n" + input_string + "\n")
    for token in tokens:
        print(token)

    print('\n')

    input_string = 'if (z > y && x = 1): a = true'

    lexer = Lexer(input_string, tokensE)
    tokens = lexer.lex()

    print("Second segment: \n" + input_string + "\n")
    for token in tokens:
        print(token)
