class Token:
    def __init__(self, tokens):
        self.tokens = tokens
    # Define a dictionary of token names and their corresponding regular expressions
    tokens = {
        'NUMBER': r'\d+(\.\d+)?',
        'PLUS': r'\+',
        'MINUS': r'\-',
        'TIMES': r'\*',
        'DIVIDE': r'/',
        'LPAREN': r'\(',
        'RPAREN': r'\)',
        'ASSIGN': r'=',
        'SEMICOLON': r';',
        'COMMA': r',',
        'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    }
