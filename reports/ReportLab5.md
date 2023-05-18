# Laboratory Work Nr.5

## Topic: Parser & Building an Abstract Syntax Tree
### Course: Formal Languages & Finite Automata
### Author: Iațco Sorin

----

## Theory
Parsing, syntax analysis, or syntactic analysis is the process of analyzing a string of symbols, either in natural 
language, computer languages or data structures, conforming to the rules of a formal grammar. The term parsing comes 
from Latin pars (orationis), meaning part (of speech).

An abstract syntax tree (AST), or just syntax tree is a tree representation of the abstract syntactic structure of 
a text (often source code) written in a formal language. Each node of the tree denotes a construct occurring in the text.

The syntax is "abstract" in the sense that it does not represent every detail appearing in the real syntax, but rather
just the structural or content-related details. For instance, grouping parentheses are implicit in the tree structure, 
so these do not have to be represented as separate nodes. Likewise, a syntactic construct like an if-condition-then 
statement may be denoted by means of a single node with three branches.

## Objectives:

1. Get familiar with parsing, what it is and how it can be programmed.
2. Get familiar with the concept of AST.
3. In addition to what has been done in the 3rd lab work, do the following:
   1. In case if there is not a type that denotes, the possible types of tokens need to:
      1. Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description

### Parser class
The class Parser defines methods for parsing a sequence of tokens into an abstract syntax tree 
(AST) representation of a Python expression or statement. The class initializes with an output tokens of the lexer with 
 which then works on, makes all the operations and the output is then saved into a .json file. The class uses the following methods. 

### peek() and get()
The peek() method returns the next token in the list without consuming it, or None if there are no more tokens. 
The get() method returns and consumes the next token in the list, or None if there are no more tokens.

### parse_expression()
This method parses a sequence of tokens into an AST node representing a Python expression. It handles multiple 
expressions separated by semicolons and returns either a single expression node or a block node containing a list of expressions.

```
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
```

### parse_comparison()
This method parses a sequence of tokens into an AST node representing a Python comparison expression. It handles operators
such as equals, not equals, less than, and greater than, and returns an operation node with the operator and the left 
and right operands.

```
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
```

### parse_term()
It handles operators such as plus and minus, and returns an operation node with the operator and the left and right operands.

### parse_factor()
This method handles operators such as times and divide, and returns an operation node with the operator and the left and right operands.

```
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
```

### parse_unary()
This method handles operators such as plus, minus, and not, and returns an operation node with the operator and the operand.

```
def parse_unary(self):
        op = self.peek()
        if op is not None and op['type'] in ['PLUS', 'MINUS', 'NOT']:
            self.get()
            operand = self.parse_unary()
            return {'type': 'operation', 'operator': op['type'], 'operand': operand}
        else:
            return self.parse_primary()
```

### parse_primary()
This method parses a sequence of tokens into an AST node representing a Python primary expression. It handles literals 
such as numbers and strings, identifiers, parentheses, and if-else expressions, and returns the corresponding node type.

```
def parse_primary(self):
        token = self.get()
        if token['type'] == 'NUMBER':
            return {'type': 'number', 'value': float(token['value'])}
        elif token['type'] == 'IDENTIFIER':
            return {'type': 'identifier', 'value': token['value']}
        ...
        elif token['type'] == 'IF':
            ...
            return {'type': 'if-else', 'condition': condition, 'if_expression': if_expr, 'else_expression': else_expr}
        else:
            raise ValueError('Invalid token: ' + token['type'])
```


## Conclusions / Results

### Conclusion
In conclusion, implementing a parser that accepts tokens produced by a lexer and generates an Abstract Syntax Tree (AST)
is a crucial step in the process of building a robust and efficient compiler or interpreter.

First of all, a lexer converts a stream of characters into tokens, which represent meaningful units in the programming 
language. This step involves identifying keywords, identifiers, literals, and other language-specific elements. 
Implementing a reliable lexer is essential for providing a consistent stream of tokens to the parser.

Secondly, the parser takes the token stream as input and constructs a hierarchical structure known as the Abstract Syntax 
Tree (AST). The parser applies a set of grammar rules to determine the structure and relationships among the tokens. 
Designing a grammar that accurately represents the language's syntax is critical for correct parsing.

Third of all, the AST represents the syntactic structure of the source code, capturing its hierarchical relationships 
and operator precedence. Each node in the AST corresponds to a language construct, such as a conditional statement, or 
variable assignment. Building the AST involves creating and linking nodes based on the grammar rules and token relationships.

Finally, implementing a parser that accepts tokens produced by a lexer and generates an AST is a critical component of 
the compilation or interpretation process. It involves tokenization, parsing based on a grammar, constructing the AST, 
semantic analysis, and more. By designing and implementing an effective parser, we can create powerful language tools that enable efficient execution or evaluation of programming code.

### Results
Input string: 'if (2 > x) : 0 else x / 2'

Output:
```
{
    {
    "type": "if-else",
    "condition": {
        "type": "operation",
        "operator": "GREATER_THAN",
        "left": {
            "type": "number",
            "value": 2.0
        },
        "right": {
            "type": "identifier",
            "value": "x"
        }
    },
    "if_expression": {
        "type": "number",
        "value": 0.0
    },
    "else_expression": {
        "type": "operation",
        "operator": "DIVIDE",
        "left": {
            "type": "identifier",
            "value": "x"
        },
        "right": {
            "type": "number",
            "value": 2.0
        }
    }
}
```

Input string: 'a + 5 != !a / 3'

Output:
```
{
    "type": "operation",
    "operator": "NOT_EQUALS",
    "left": {
        "type": "operation",
        "operator": "PLUS",
        "left": {
            "type": "identifier",
            "value": "a"
        },
        "right": {
            "type": "number",
            "value": 5.0
        }
    },
    "right": {
        "type": "operation",
        "operator": "DIVIDE",
        "left": {
            "type": "operation",
            "operator": "NOT",
            "operand": {
                "type": "identifier",
                "value": "a"
            }
        },
        "right": {
            "type": "number",
            "value": 3.0
        }
    }
}
```

Input string: '"hello" + "world"'

Output:
```
{
    "type": "operation",
    "operator": "PLUS",
    "left": {
        "type": "string",
        "value": "hello"
    },
    "right": {
        "type": "string",
        "value": "world"
    }
}
```

## References
https://github.com/DrVasile/FLFA-Labs/blob/master/5_ParserASTBuild/task.md
