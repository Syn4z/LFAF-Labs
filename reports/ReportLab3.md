# Laboratory Work Nr.3

### Course: Formal Languages & Finite Automata
### Author: Iatco Sorin

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

* Understand what lexical analysis is.
***  
* Get familiar with the inner workings of a lexer/scanner/tokenizer.

***
* Implement a sample lexer and show how it works.


## Implementation description

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

## Conclusions / Results

### Conclusion
A crucial step in creating a compiler or interpreter for a computer language is the implementation of a lexer. I
gain practical experience using regular expressions and creating software tools for parsing and analyzing code in a 
laboratory setting by designing a lexer.

By using a lexer, we learn how a compiler or interpreter's lexical analysis phase functions and how regular 
expressions can be used to specify a computer language's grammar. Furthermore, I learn the value of error handling 
and how to create a lexer that can identify and communicate input code mistakes.

In addition to implementing a lexer, a laboratory assignment on this topic may also include exercises on building a 
parser and interpreter for the programming language. This provides us with a complete understanding of the 
compilation process and how the different phases of a compiler work together to translate source code into executable code.

Finally, a lexer implementation lab assignment is a crucial component of a computer science or software engineering
program and gives students invaluable hands-on practice creating software tools for parsing and analyzing code.

### Results


## References
https://github.com/DrVasile/FLFA-Labs/blob/master/3_LexerScanner/task.md