import re

from src.lexer.Lexer import Lexer
from src.lexer.Token import Token
from src.parser.Parser import Parser

if __name__ == '__main__':

    input_string = '3+-*/()==!==;":,<=><>=ifelsewhileforfunctionreturn&&||!truefalseidentifier'
    tokensE = Token.tokens
    tokens = re.findall(r'[\w.]+|[-+*/=();:]', input_string)
    print(tokens)

    lexer = Lexer(input_string, tokensE)
    token = lexer.lex()

    number_3 = Parser(Lexer(input_string, tokensE))
    print(number_3)

    print("Segment 1: \n" + input_string + "\n" + "\nTokens:")
    for token in token:
        print(token)
