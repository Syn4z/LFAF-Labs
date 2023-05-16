from src.parser.AST import Number, BinaryOperation


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def parse(self):
        self.advance()
        return self.expression()

    def advance(self):
        self.current_token = self.lexer.getChar()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected {token_type}, but found {self.current_token.type}")

    def factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node

    def term(self):
        node = self.factor()
        while self.current_token.type in ['TIMES', 'DIVIDE']:
            token = self.current_token
            if token.type == 'TIMES':
                self.eat('TIMES')
            elif token.type == 'DIVIDE':
                self.eat('DIVIDE')
            node = BinaryOperation(left=node, op=token.value, right=self.factor())
        return node

    def expression(self):
        node = self.term()
        while self.current_token.type in ['PLUS', 'MINUS']:
            token = self.current_token
            if token.type == 'PLUS':
                self.eat('PLUS')
            elif token.type == 'MINUS':
                self.eat('MINUS')
            node = BinaryOperation(left=node, op=token.value, right=self.term())
        return node
