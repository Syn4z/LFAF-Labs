import json
import os
from src.lexer.Lexer import Lexer
from src.lexer.Token import Token
from src.parser.Parser import Parser

if __name__ == '__main__':

    # Input strings
    input_string1 = 'if (2 > x) : 0 else x / 2'
    input_string2 = 'a + 5 != !a / 3'
    input_string3 = '"hello" + "world"'
    input_string4 = 'a * 3; b - 9; !p < 2'

    # Initialize lexer and parser
    lexer = Lexer(input_string1, Token.tokens)
    parser = Parser(lexer.lex())

    # Parse input string
    ast = parser.parse_expression()

    # Create .json file to store AST
    directory = 'ast'
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(directory, 'ast.json')
    with open(filename, 'w') as f:
        json.dump(ast, f, indent=4)
