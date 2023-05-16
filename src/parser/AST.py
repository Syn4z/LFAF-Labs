class Number:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression


class IfElseStatement:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
