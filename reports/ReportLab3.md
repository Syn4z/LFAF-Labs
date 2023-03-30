# Laboratory Work Nr.3

### Course: Formal Languages & Finite Automata
### Author: Iațco Sorin

----

## Theory
A lexer, also known as a lexical analyzer, is an essential component of a compiler or interpreter. It is responsible for
breaking down the input program into a sequence of tokens, which are meaningful units of the programming language, such 
as keywords, identifiers, operators, and literals. The process of generating tokens from the input program is called 
lexical analysis.

The implementation of a lexer involves several steps. First, the input program is read character by character. Then, the
characters are grouped into tokens based on predefined patterns, which are expressed using regular expressions. These 
patterns define the syntax of the programming language, including keywords, operators, and other language constructs.

The lexer typically maintains a buffer that holds a portion of the input program that has been read but not yet tokenized.
It also maintains a state machine that keeps track of the current state of the lexer, based on the patterns of the tokens
encountered so far. The state machine determines which pattern to apply next based on the current state and the next character
in the input stream.

As each token is generated, it is passed to the parser for further processing. The parser uses the sequence of tokens to
build a syntax tree or abstract syntax tree that represents the structure of the input program.

## Objectives:

1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.


## Implementation description

### Lexer class
This code defines a class called Lexer that is used to break down an input string into a sequence of tokens based on a 
set of predefined regular expression patterns. The Lexer class takes two parameters in its constructor: the input string
to be tokenized and a dictionary of token expressions, where each key-value pair represents a token name and its 
corresponding regular expression pattern.

```
class Lexer:
    def __init__(self, inputString, tokenExpressions):
        self.inputString = inputString
        self.tokenExpressions = tokenExpressions
```

### Lexer methods
The Lexer class defines a method called lex() that generates the tokens from the input string. The method works by 
iterating over the input string and checking each character against the predefined regular expression patterns. If a 
match is found, the corresponding token is added to a list of tokens, along with the matched text.

The lex() method uses several helper functions to handle different aspects of the tokenization process. The getChar() 
function is used to retrieve the next character from the input string, while the peek() function is used to peek at the
next character without consuming it. The skip_whitespace() function is used to skip over any whitespace and comments in 
the input string, while the match() function is used to match a regular expression pattern and return the matched text.

```
        def getChar():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            c = self.inputString[pos]
            pos += 1
            return c

        def peek():
            nonlocal pos
            if pos >= len(self.inputString):
                return None
            return self.inputString[pos]

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

        def match(pattern):
            nonlocal pos
            m = re.match(pattern, self.inputString[pos:])
            if m is not None:
                content = m.group(0)
                pos += len(content)
                return content
            else:
                return None
```

### Lexer logic
The lex() method uses a while loop to iterate over the input string and generate tokens. It first calls skip_whitespace()
to skip over any whitespace and comments. It then checks if there are any characters left in the input string. If not, 
the loop breaks and the method returns the list of tokens. If there are characters left, the method iterates over each 
token expression in the dictionary and attempts to match it against the input string using the match() function. If a 
match is found, the corresponding token is added to the list of tokens and the loop breaks. If no match is found, an 
error is raised indicating that an invalid character was encountered at a specific line and column in the input string.

```
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
```

### Token
The class called Token has a dictionary 'tokens' as a class attribute. The tokens dictionary maps names of tokens
to their corresponding regular expressions. The regular expressions defined in the tokens dictionary are used to match 
and identify tokens in the input source code.
```
...
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
        ...
```


## Conclusions / Results

### Conclusion
In conclusion, this laboratory work proves that the crucial step in creating a compiler or interpreter for a computer language
is the implementation of a lexer. I gain practical experience using regular expressions and creating software tools for 
analyzing code in a laboratory setting by designing a lexer.

By using a lexer, we learn how a compiler or interpreter's lexical analysis phase functions and how regular 
expressions can be used to specify a computer language's grammar. Furthermore, I learn the value of error handling 
and how to create a lexer that can identify and communicate input code mistakes.

Moreover, understanding the relationship between lexemes and tokens can help in building a lexer that can identify and
classify different types of tokens in an input program. This is an important skill for me that helped in building a lexer
with tokens and understand its functionality.

Finally, a lexer implementation is an essential component of a computer science or software engineering program because it 
provides with hands-on practice in creating software tools for parsing and analyzing code. This type of practical
experience was invaluable for me, as it helped me develop a deeper understanding of how programming languages work and 
how they can be analyzed and manipulated.

### Results
Segment 1: 
x = 3 + 4 * 2; y = x / (5 - 2);

Tokens:

('Input: x', 'Token: IDENTIFIER')
('Input: =', 'Token: ASSIGN')
('Input: 3', 'Token: NUMBER')
('Input: +', 'Token: PLUS')
('Input: 4', 'Token: NUMBER')
('Input: *', 'Token: TIMES')
('Input: 2', 'Token: NUMBER')
('Input: ;', 'Token: SEMICOLON')
('Input: y', 'Token: IDENTIFIER')
('Input: =', 'Token: ASSIGN')
('Input: x', 'Token: IDENTIFIER')
('Input: /', 'Token: DIVIDE')
('Input: (', 'Token: LPAREN')
('Input: 5', 'Token: NUMBER')
('Input: -', 'Token: MINUS')
('Input: 2', 'Token: NUMBER')
('Input: )', 'Token: RPAREN')
('Input: ;', 'Token: SEMICOLON')


Segment 2: 
if (z > y && x == 1): a = true else: print("Wrong", b)

Tokens:

('Input: if', 'Token: IF')
('Input: (', 'Token: LPAREN')
('Input: z', 'Token: IDENTIFIER')
('Input: >', 'Token: GREATER_THAN')
('Input: y', 'Token: IDENTIFIER')
('Input: &&', 'Token: AND')
('Input: x', 'Token: IDENTIFIER')
('Input: ==', 'Token: EQUALS')
('Input: 1', 'Token: NUMBER')
('Input: )', 'Token: RPAREN')
('Input: :', 'Token: COLON')
('Input: a', 'Token: IDENTIFIER')
('Input: =', 'Token: ASSIGN')
('Input: true', 'Token: TRUE')
('Input: else', 'Token: ELSE')
('Input: :', 'Token: COLON')
('Input: print', 'Token: IDENTIFIER')
('Input: (', 'Token: LPAREN')
('Input: "', 'Token: QUOTATION')
('Input: Wrong', 'Token: IDENTIFIER')
('Input: "', 'Token: QUOTATION')
('Input: ,', 'Token: COMMA')
('Input: b', 'Token: IDENTIFIER')
('Input: )', 'Token: RPAREN')


Segment 3: 
function alpha(): return 1, true

Tokens:

('Input: function', 'Token: FUNCTION')
('Input: alpha', 'Token: IDENTIFIER')
('Input: (', 'Token: LPAREN')
('Input: )', 'Token: RPAREN')
('Input: :', 'Token: COLON')
('Input: return', 'Token: RETURN')
('Input: 1', 'Token: NUMBER')
('Input: ,', 'Token: COMMA')
('Input: true', 'Token: TRUE')


Segment 4: 
while(a != 0 || a == !b): sum = a + b return sum

Tokens:

('Input: while', 'Token: WHILE')
('Input: (', 'Token: LPAREN')
('Input: a', 'Token: IDENTIFIER')
('Input: !=', 'Token: NOT_EQUALS')
('Input: 0', 'Token: NUMBER')
('Input: ||', 'Token: OR')
('Input: a', 'Token: IDENTIFIER')
('Input: ==', 'Token: EQUALS')
('Input: !', 'Token: NOT')
('Input: b', 'Token: IDENTIFIER')
('Input: )', 'Token: RPAREN')
('Input: :', 'Token: COLON')
('Input: sum', 'Token: IDENTIFIER')
('Input: =', 'Token: ASSIGN')
('Input: a', 'Token: IDENTIFIER')
('Input: +', 'Token: PLUS')
('Input: b', 'Token: IDENTIFIER')
('Input: return', 'Token: RETURN')
('Input: sum', 'Token: IDENTIFIER')

## References
https://github.com/DrVasile/FLFA-Labs/blob/master/3_LexerScanner/task.md