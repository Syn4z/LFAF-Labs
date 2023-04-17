# Laboratory Work Nr.4

### Topic: Chomsky Normal Form
### Course: Formal Languages & Finite Automata
### Author: Iațco Sorin
### Variant: 21

----

## Theory
In formal language theory, a context-free grammar G is said to be in Chomsky normal form if all of its production rules are of the form:

A → BC,   or
A → a,   or
S → ε,

Where A, B, and C are non-terminal symbols, an is a terminal symbol,
S is the start symbol, and ε denotes the empty string. Also, neither B nor C may be the start symbol, and the third 
production rule can only appear if ε is in L(G), the language produced by the context-free grammar G.

Every grammar in Chomsky normal form is context-free, and conversely, every context-free grammar can be transformed into
an equivalent one which is in Chomsky normal form and has a size no larger than the square of the original grammar's size.

## Objectives:

1. Learn about Chomsky Normal Form (CNF).
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
   1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
   2. The implemented functionality needs executed and tested.
   3. BONUS. Unit tests that validate the functionality of the project.
   4. BONUS. Make the aforementioned function to accept any grammar, not only the one from the specific variant.


## Implementation description

### removeEpsilon()
This function first identifies which variables can derive epsilon by searching for the symbol "ε" in the right-hand side
of each production rule. These variables are stored in the set "epsilon".

Next, the function iterates over each production rule and each symbol on the right-hand side of that rule. For each 
symbol that contains a variable that can derive epsilon, the algorithm replaces that variable with the empty string and
adds the modified symbol to the right-hand side of the production rule. If the current symbol is already epsilon, it is 
simply removed from the right-hand side of the production rule.

```
...
for variable, productions in self.productions.items():
            if "ε" in productions:
                epsilon.add(variable)

        for left, right in self.productions.items():
            for i in right:
                for j in epsilon:
                    if j in i:
                        if left == j:
                            break
                        self.productions[left] = [x.replace(j, "") for x in self.productions[left]]
                        self.productions[left].append(i)
                    elif i == "ε":
                        self.productions[left].remove(i)
        ...                
```

### removeUnit()
The method is for removing the unit productions, contains a "for" loop that iterates over the dictionary "productions", which stores the set of 
production rules.

Inside the "for" loop, there's another "for" loop that iterates over each right-hand side sequence in the current 
production rule. If the sequence contains only one symbol (i.e., it's a unit production) and that symbol is a non-terminal,
the method performs a replacement operation: it removes the unit production from the current right-hand side and replaces
it with the right-hand sides of the non-terminal it represents.

The method then calls itself recursively, and returns the modified "productions" dictionary.

```
   ...
        for left, right in self.productions.items():
            # In my variant I have no inner loops occurring, so I can just replace the unit productions
            # with the right hand side of the specific production
            for e in right:
                if len(e) == 1 and e in self.nonTerminal:
                    self.productions[left].remove(e)
                    self.productions[left].extend(self.productions[e])
                    self.removeUnit()
        ...            
```

### removeInaccessible()
The function removes all the inaccessible symbols, first creates a set named accessible to hold all the accessible symbols. It then iterates over each 
production in the object's productions dictionary and checks each symbol in the right-hand side of the production to see
if it is accessible. If a symbol is accessible, it is added to the accessible set.

After identifying all the accessible symbols, the method then iterates over each production again and checks each
symbol on the left-hand side. If a symbol is not in the accessible set, it is deleted from the productions' dictionary. 
If any symbols are deleted, the updated productions dictionary is returned.

```
   ...
        for left, right in self.productions.items():
            # For each production, iterate over each symbol in the right-hand side
            for r in right:
                for w in r:
                    # If the symbol is accessible, add it to the 'accessible' set
                    accessible.add(w)

        # Iterate over each production in the 'productions' dictionary again
        for left, right in self.productions.items():
            # For each production, iterate over each symbol on the left-hand side
            for a in left:
                # If the symbol is accessible, continue to the next symbol
                if a in accessible:
                    continue
                # If the symbol is not accessible, delete it from the 'productions' dictionary
                else:
                    del self.productions[a]
                    del self.nonTerminal[self.nonTerminal.index(a)]
                    # Return the updated 'productions' dictionary if any symbols are deleted
                    return self.productions
        ...            
```

### removeNonProductive()
This function removes any unproductive symbols, first creates a set named productive to hold all the productive symbols. It then iterates over each 
production in the object's productions dictionary and checks if any right-hand symbol is a terminal symbol. If it is, 
the left-hand symbol is added to the productive set.

After identifying all the productive symbols, the method iterates over each production again and checks each
left-hand symbol. If a left-hand symbol is not in the productive set, it is deleted from the productions' dictionary. 
If any symbols are deleted, the updated productions dictionary is returned.

For each right-hand symbol, the method replaces any unproductive non-terminal symbols with empty strings. Additionally, 
if a symbol is a terminal symbol and is not yet on the right-hand side, it is added. If a symbol is a terminal symbol
and is already on the right-hand side, it is removed. Finally, the updated right-hand side symbols are added to a new list,
which is then used to update the productions' dictionary.
```
      ...
            for r in right:
                if len(r) > 1:
                    for w in r:
                        if w in self.nonTerminal:
                            if w in new_right:
                                break
                            elif w not in productive:
                                new_right.append(r.replace(w, ""))
                        elif w in self.terminal and w not in self.productions[left]:
                            new_right.append(r.replace(r, w))
                        elif w in self.terminal and w in self.productions[left]:
                            if len(r) > 2:
                                continue
                            new_right.append(r.replace(w, ""))
                        else:
                            continue
                else:
                    new_right.append(r)
            ...              
```

### toChomskyNormalForm()
Finally, this function returns the converted grammar in the Chomsky Normal Form, with all the productions, terminal and
non-terminal symbols respectively. It calls all the functions necessary for this procedure. 

```
def toChomskyNormalForm(self):
        self.removeEpsilon()
        print("\nAfter removing epsilon: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)
        ...
        
        self.removeNonProductive()
        print("\nAfter removing non-productive: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)
        ...
```

### UnitTest()
In this class are all the unit tests for the functions implemented in the previous classes. The tests are performed on all
the functions, and the results are printed in the console. All the tests are methods.

```
class UnitTest(unittest.TestCase):
   ...
   def test_grammar(self):
        ...
    
    def test_to_chomsky_normal_form(self):
        ...
if __name__ == '__main__':
    unittest.main()
```


## Conclusions / Results

### Conclusion
In conclusion, implementing Chomsky Normal Form is an important step in simplifying and standardizing context-free 
grammars for computational processing. The process involves several steps, including removing epsilon productions, 
unit productions, inaccessible productions, and non-productive productions.

Firstly, by converting a context-free grammar into Chomsky Normal Form, we can ensure that it meets certain criteria for efficient
parsing and processing, which is important in areas such as natural language processing and computational linguistics.

Next, implementing Chomsky Normal Form requires a good understanding of the principles of context-free grammars and the 
specific steps involved in the conversion process. The code provided in the laboratory work demonstrates how the 
necessary functions can be implemented in a programming language to automate the conversion process.

Lastly, in this laboratory work I managed to implement with success all the task required and to obtain the Chomsky Normal
Form for the given grammar.

### Results
Initial Grammar: 

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B', 'C', 'D']

Productions:  {'S': ['dB', 'AC'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC'], 'D': ['ab'], 'C': ['bC', 'ε']}

--------------------


After removing epsilon:

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B', 'C', 'D']

Productions:  {'S': ['dB', 'A', 'AC'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'A', 'AC'], 'D': ['ab'], 'C': ['bC']}

--------------------

After removing unit productions:

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B', 'C', 'D']

Productions:  {'S': ['dB', 'AC', 'd', 'dS', 'aBdB'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC', 'd', 'dS', 'aBdB'], 'D': ['ab'], 'C': ['bC']}

--------------------

After removing inaccessible:

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B', 'C']

Productions:  {'S': ['dB', 'AC', 'd', 'dS', 'aBdB'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC', 'd', 'dS', 'aBdB'], 'C': ['bC']}

--------------------

After removing non-productive:

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B']

Productions:  {'S': ['B', 'A', 'd', 'S', 'a'], 'A': ['d', 'S', 'a'], 'B': ['a', 'A', 'd', 'S']}

----------------------
----------------------

Chomsky Normal Form:

Terminal:  ['a', 'b', 'd']

Non-terminal:  ['S', 'A', 'B']

Productions:  {'S': ['B', 'A', 'd', 'S', 'a'], 'A': ['d', 'S', 'a'], 'B': ['a', 'A', 'd', 'S']}

### Unit Tests
Ran 10 tests in 0.004s

OK

## References
https://github.com/DrVasile/FLFA-Labs/blob/master/4_ChomskyNormalForm/task.md