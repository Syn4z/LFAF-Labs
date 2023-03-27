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
        'ASSIGN': r'=',
        'SEMICOLON': r';',
        'COLON': r':',
        'COMMA': r',',
        'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'EQUALS': r'==',
        'NOT_EQUALS': r'!=',
        'LESS_THAN': r'<',
        'LESS_THEN_EQUALS': r'<=',
        'GREATER_THAN': r'>',
        'GREATER_THAN_EQUAL': r'>=',
        'IF': r'if',
        'ELSE': r'else',
        'WHILE': r'while',
        'FOR': r'for',
        'FUNCTION': r'function',
        'RETURN': r'return',
        'AND': r'&&',
        'OR': r'\|\|',
        'NOT': r'!',
        'TRUE': r'true',
        'FALSE': r'false',
    }

    def getType(self):
        return self.tokens.keys()

    def getLexeme(self):
        return self.tokens.values()
