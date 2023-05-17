import json
import os
from src.lexer.Lexer import Lexer
from src.lexer.Token import Token
from src.parser.Parser import Parser

if __name__ == '__main__':

    input_string1 = 'if (2 > x) : 0 else x / 2'
    input_string2 = 'a + 5 != !a / 3'
    input_string3 = '"hello" + "world"'
    input_string4 = 'a * 3; b - 9'
    tokensE = Token.tokens

    lexer = Lexer(input_string1, tokensE)
    tokens = lexer.lex()

    parser = Parser(tokens)
    ast = parser.parse_expression()

    directory = 'ast'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, 'ast.json')

    with open(filename, 'w') as f:
        json.dump(ast, f, indent=4)
