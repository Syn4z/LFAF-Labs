from src.lexer.Lexer import Lexer
from src.lexer.Token import Token

if __name__ == '__main__':

    input_string = 'x = 3 + 4 * 2; y = x - 5;'
    tokensE = Token.tokens

    lexer = Lexer(input_string, tokensE)
    tokens = lexer.lex()

    for token in tokens:
        print(token)

    print('\n')

    input_string = 'y = 9 - 7; z = 7 / 1;'

    lexer = Lexer(input_string, tokensE)
    tokens = lexer.lex()

    for token in tokens:
        print(token)
