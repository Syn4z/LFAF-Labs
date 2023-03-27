import re


class Lexer:
    def __init__(self, inputString, tokenExpressions):
        self.inputString = inputString
        self.tokenExpressions = tokenExpressions

    # Define a function that takes the input string and generates tokens
    def lex(self):
        tokens = []
        pos = 0
        lineNr = 1
        lineStart = 0

        # Define a function to get the next character from the input string
        def getChar():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            char = self.inputString[pos]
            pos += 1
            return char

        # Define a function to peek at the next character in the input string
        def peek():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            return self.inputString[pos]

        # Define a function to skip whitespace and comments
        def skip_whitespace():
            nonlocal lineNr, lineStart
            while True:
                char = peek()
                if char is None:
                    return
                if char.isspace():
                    if char == '\n':
                        lineNr += 1
                        lineStart = pos
                    getChar()
                elif char == '#':
                    while char is not None and char != '\n':
                        char = getChar()
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

        # Define a loop that generates the tokens
        while True:
            skip_whitespace()
            if peek() is None:
                break
            for token, pattern in self.tokenExpressions.items():
                text = match(pattern)
                if text is not None:
                    tokens.append(("Token: " + token, "Input: " + str(text)))
                    break
            else:
                raise ValueError(f"Invalid character '{peek()}' at line {lineNr}, column {pos - lineStart}")

        return tokens
