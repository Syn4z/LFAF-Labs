class Token:
    def __init__(self, tokens):
        self.tokens = tokens

    tokens = {
        'NUMBER': r'\d+(\.\d+)?',
        'PLUS': r'\+',
        'MINUS': r'\-',
        'TIMES': r'\*',
        'DIVIDE': r'/',
        'LPAREN': r'\(',
        'RPAREN': r'\)',
        'EQUALS': r'==',
        'NOT_EQUALS': r'!=',
        'ASSIGN': r'=',
        'SEMICOLON': r';',
        'QUOTATION': r'"',
        'COLON': r':',
        'COMMA': r',',
        'LESS_THAN': r'<',
        'GREATER_THAN': r'>',
        'IF': r'if',
        'ELSE': r'else',
        'AND': r'&&',
        'OR': r'\|\|',
        'NOT': r'!',
        'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    }
