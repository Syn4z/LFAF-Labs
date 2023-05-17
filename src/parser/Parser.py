class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def get(self):
        token = self.peek()
        if token is not None:
            self.pos += 1
        return token

    def parse_expression(self):
        expressions = []
        while True:
            expression = self.parse_comparison()
            expressions.append(expression)
            next_token = self.peek()
            if next_token is None or next_token['type'] != 'SEMICOLON':
                break
            self.get()
        if len(expressions) == 1:
            return expressions[0]
        else:
            return {'type': 'block', 'expressions': expressions}

    def parse_comparison(self):
        left = self.parse_term()
        while True:
            op = self.peek()
            if op is None or op['type'] not in ['EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN']:
                break
            self.get()
            right = self.parse_term()
            left = {'type': 'operation', 'operator': op['type'], 'left': left, 'right': right}
        return left

    def parse_term(self):
        left = self.parse_factor()
        while True:
            op = self.peek()
            if op is None or op['type'] not in ['PLUS', 'MINUS']:
                break
            self.get()
            right = self.parse_factor()
            left = {'type': 'operation', 'operator': op['type'], 'left': left, 'right': right}
        return left

    def parse_factor(self):
        left = self.parse_unary()
        while True:
            op = self.peek()
            if op is None or op['type'] not in ['TIMES', 'DIVIDE']:
                break
            self.get()
            right = self.parse_unary()
            left = {'type': 'operation', 'operator': op['type'], 'left': left, 'right': right}
        return left

    def parse_unary(self):
        op = self.peek()
        if op is not None and op['type'] in ['PLUS', 'MINUS', 'NOT']:
            self.get()
            operand = self.parse_unary()
            return {'type': 'operation', 'operator': op['type'], 'operand': operand}
        else:
            return self.parse_primary()

    def parse_primary(self):
        token = self.get()
        if token['type'] == 'NUMBER':
            return {'type': 'number', 'value': float(token['value'])}
        elif token['type'] == 'IDENTIFIER':
            return {'type': 'identifier', 'value': token['value']}
        elif token['type'] == 'LPAREN':
            expr = self.parse_expression()
            if self.get()['type'] != 'RPAREN':
                raise ValueError('Expected right parenthesis')
            return expr
        elif token['type'] == 'QUOTATION':
            value = ''
            while True:
                token = self.get()
                if token is None:
                    raise ValueError('Expected closing quotation mark')
                if token['type'] == 'QUOTATION':
                    break
                value += token['value']
            return {'type': 'string', 'value': value}
        elif token['type'] == 'IF':
            condition = self.parse_expression()
            if_token = self.get()
            if if_token['type'] != 'COLON':
                raise ValueError('Expected "COLON" after "IF" condition')
            if_expr = self.parse_expression()
            else_token = self.get()
            if else_token['type'] != 'ELSE':
                raise ValueError('Expected "ELSE" after "IF" expression')
            else_expr = self.parse_expression()
            return {'type': 'if-else', 'condition': condition, 'if_expr': if_expr, 'else_expr': else_expr}
        else:
            raise ValueError('Invalid token: ' + token['type'])
