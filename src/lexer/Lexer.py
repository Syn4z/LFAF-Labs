import re


class Lexer:
    def __init__(self, inputString, tokenExpressions):
        self.inputString = inputString
        self.tokenExpressions = tokenExpressions

    # Define a function that takes the input string and generates tokens
    def lex(self):
        tokens = []
        pos = 0
        line_num = 1
        line_start = 0

        # Define a function to get the next character from the input string
        def getChar():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            c = self.inputString[pos]
            pos += 1
            return c

        # Define a function to peek at the next character in the input string
        def peek():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            return self.inputString[pos]

        # Define a function to skip whitespace and comments
        def skip_whitespace():
            nonlocal line_num, line_start
            while True:
                c = peek()
                if c is None:
                    return
                if c.isspace():
                    if c == '\n':
                        line_num += 1
                        line_start = pos
                    getChar()
                elif c == '#':
                    while c is not None and c != '\n':
                        c = getChar()
                else:
                    return

        # Define a function to match a regular expression pattern and return the matched text
        def match(pattern):
            nonlocal pos
            m = re.match(pattern, self.inputString[pos:])
            if m is not None:
                content = m.group(0)
                pos += len(content)
                return content
            else:
                return None

        # Define a loop that generates tokens
        while True:
            skip_whitespace()
            if peek() is None:
                break
            for token, pattern in self.tokenExpressions.items():
                text = match(pattern)
                if text is not None:
                    tokens.append((token, text))
                    break
            else:
                raise ValueError(f"Invalid character '{peek()}' at line {line_num}, column {pos - line_start}")

        return tokens
