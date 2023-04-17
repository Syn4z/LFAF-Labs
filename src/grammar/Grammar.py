from src.automaton.FiniteAutomaton import FiniteAutomaton
from typing import List, Dict
import random


class Grammar:
    def __init__(self, startSymbol: str, terminal: List[str], nonTerminal: List[str],
                 productions: Dict[str, List[str]]):
        self.startSymbol = startSymbol
        self.terminal = terminal
        self.nonTerminal = nonTerminal
        self.productions = productions

    def generateWord(self) -> str:
        return self.generateWordHelper(self.startSymbol)

    def generateWordHelper(self, character) -> str:
        if character in self.terminal:
            return character
        rightSide = self.productions[character]
        randomRightSide = random.choice(rightSide)
        word = ''
        newRightSide = []
        if "q" in character:
            for nr, el in enumerate(randomRightSide):
                if el == 'q':
                    newRightSide = [randomRightSide[:nr], randomRightSide[nr:]]
        else:
            newRightSide = randomRightSide
        for rightChar in newRightSide:
            word += self.generateWordHelper(rightChar)
        return word

    def toFiniteAutomaton(self):
        states = set()
        finalStates = {'X'}
        dimension = 0
        transitions = []
        for nonTerminal in self.nonTerminal:
            dimension += len(self.productions[nonTerminal])
        for nonTerminal in self.nonTerminal:
            states.add(nonTerminal)
            rightHandSides = self.productions[nonTerminal]
            for rightSide in rightHandSides:
                if len(rightSide) > 1:
                    nextState = rightSide[1]
                else:
                    nextState = 'X'
                transitionLabel = rightSide[0]
                transitions.append((nonTerminal, transitionLabel, nextState))
        states.add('X')
        automaton = FiniteAutomaton(states, self.terminal, transitions, self.startSymbol, finalStates)
        automaton.setStates(states)
        automaton.setStartState(str(self.startSymbol))
        automaton.setAcceptStates(finalStates)
        automaton.setAlphabet(self.terminal)
        return automaton

    def classifyGrammar(self):
        # Check if the grammar is a Type 3 grammar
        is_type_3 = True
        for nonTerminal in self.nonTerminal:
            for production in self.productions[nonTerminal]:
                if len(production) > 2 or (production[0] not in self.terminal and production[0]
                                           not in self.nonTerminal) or (
                        len(production) == 2 and production[1] not in self.nonTerminal):
                    is_type_3 = False
                    break
        if is_type_3:
            return 'Type 3'

        # Check if the grammar is a Type 2 grammar
        is_type_2 = True
        for nonTerminal in self.nonTerminal:
            if nonTerminal != self.startSymbol:
                if len(self.productions[nonTerminal]) > 1:
                    is_type_2 = False
                    break
                production = self.productions[nonTerminal][0]
                if len(production) != 1 or (
                        production[0] not in self.terminal and production[0] not in self.nonTerminal):
                    is_type_2 = False
                    break
        if is_type_2:
            return 'Type 2'

        # Check if the grammar is a Type 1 grammar
        is_type_1 = True
        for nonTerminal in self.nonTerminal:
            for production in self.productions[nonTerminal]:
                if len(production) < 1 or (
                        production[0] not in self.terminal and production[0] not in self.nonTerminal):
                    is_type_1 = False
                    break
                for symbol in production[1:]:
                    if symbol not in self.nonTerminal:
                        is_type_1 = False
                        break
        if is_type_1:
            return 'Type 1'

        # Check if the grammar is a Type 0 grammar
        is_type_0 = True
        for nonTerminal in self.nonTerminal:
            for production in self.productions[nonTerminal]:
                for symbol in production:
                    if symbol not in self.terminal and symbol not in self.nonTerminal:
                        is_type_0 = False
                        break
        if is_type_0:
            return 'Type 0'

        # If the grammar does not fit into any of the types, return None
        return 'Type None'

    def toChomskyNormalForm(self):
        # Remove all epsilon productions
        self.removeEpsilon()
        print("\nAfter removing epsilon: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)

        # Remove all unit productions
        self.removeUnit()
        print("\nAfter removing unit productions: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)

        # Remove all inaccessible productions
        self.removeInaccessible()
        print("\nAfter removing inaccessible: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)

        # Remove all non-productive productions
        self.removeNonProductive()
        print("\nAfter removing non-productive: \n" + "Terminal: ", self.terminal, "\nNon-terminal: ", self.nonTerminal,
              "\nProductions: ", self.productions)

        return self.productions, self.terminal, self.nonTerminal

    def removeEpsilon(self):
        # Create a set to hold variables that can derive epsilon
        epsilon = set()

        # Identify variables that can derive epsilon
        for variable, productions in self.productions.items():
            if "ε" in productions:
                epsilon.add(variable)

        # Iterate over each production rule in the grammar
        for left, right in self.productions.items():
            # Iterate over each symbol in the right-hand side of the production rule
            for i in right:
                for j in epsilon:
                    # If the current symbol contains a variable that can derive epsilon
                    if j in i:
                        # If the current variable is the same as the left-hand side of the production rule,
                        # skip this iteration (prevents infinite loop)
                        if left == j:
                            break
                        # Replace the variable that derives epsilon with the empty string in the current symbol
                        self.productions[left] = [x.replace(j, "") for x in self.productions[left]]
                        # Add the modified symbol to the right-hand side of the production rule
                        self.productions[left].append(i)
                    # If the current symbol is epsilon, remove it from the right-hand side of the production rule
                    elif i == "ε":
                        self.productions[left].remove(i)

        return self.productions

    def removeUnit(self):
        for left, right in self.productions.items():
            # In my variant I have no inner loops occurring, so I can just replace the unit productions
            # with the right-hand side of the specific production
            for e in right:
                if len(e) == 1 and e in self.nonTerminal:
                    # Remove the current unit production
                    self.productions[left].remove(e)
                    self.productions[left].extend(self.productions[e])
                    # Recursively call removeUnit to handle nested unit productions
                    self.removeUnit()

        return self.productions

    def removeInaccessible(self):
        # Create a set to hold all the accessible symbols
        accessible = set()

        # Iterate over each production in the 'productions' dictionary
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

        return self.productions

    def removeNonProductive(self):
        # This set is for storing the productive symbols
        productive = set()

        # First, find all symbols that are reachable from the start symbol
        for left, right in self.productions.items():
            for r in right:
                # If the right-hand side consists only of terminal symbols, add the left-hand symbol to 'productive'
                if r in self.terminal:
                    productive.add(left)

        # Then, find all symbols that are reachable from the productive symbols
        for left, right in self.productions.items():
            new_right = []
            # For each left-hand symbol, check if it is in 'productive'
            for lt in left:
                if lt not in productive:
                    # If it is not in 'productive', delete it from the 'productions' dictionary
                    del self.productions[lt]
                    del self.nonTerminal[self.nonTerminal.index(lt)]
                    return self.productions

            # For each right-hand symbol, replace any unproductive non-terminal symbols with empty strings
            for r in right:
                if len(r) > 1:
                    for w in r:
                        if w in self.nonTerminal:
                            if w in new_right:
                                break
                            elif w not in productive:
                                new_right.append(r.replace(w, ""))
                        # If the symbol is a terminal symbol and is not yet in the right-hand side, add it
                        elif w in self.terminal and w not in self.productions[left]:
                            new_right.append(r.replace(r, w))
                        # If the symbol is a terminal symbol and is already in the right-hand side, remove it
                        elif w in self.terminal and w in self.productions[left]:
                            if len(r) > 2:
                                continue
                            new_right.append(r.replace(w, ""))
                        else:
                            continue
                else:
                    new_right.append(r)

            self.productions[left] = new_right

        return self.productions
