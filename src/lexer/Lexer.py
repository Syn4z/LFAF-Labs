import re


class Lexer:
    def __init__(self, inputString, tokenExpressions):
        self.inputString = inputString
        self.tokenExpressions = tokenExpressions

    def lex(self):
        tokens = []
        pos = 0
        lineNr = 1
        lineStart = 0

        def getChar():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            char = self.inputString[pos]
            pos += 1
            return char

        def peek():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            return self.inputString[pos]

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

        def match(pattern):
            nonlocal pos
            m = re.match(pattern, self.inputString[pos:])
            if m is not None:
                content = m.group(0)
                pos += len(content)
                return content
            else:
                return None

        while True:
            skip_whitespace()
            if peek() is None:
                break
            for token, pattern in self.tokenExpressions.items():
                text = match(pattern)
                if text is not None:
                    tokens.append({'type': token, 'value': text})
                    break
            else:
                raise ValueError(f"Invalid character '{peek()}' at line {lineNr}, column {pos - lineStart}")

        return tokens
