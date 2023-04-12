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

        # Remove all unit productions
        self.removeUnit()

        # Remove all inaccessible productions
        #self.removeInaccessible()

        # Remove all non-productive productions
        #self.removeNonProductive()

        return self.productions

    def removeEpsilon(self):
        epsilon = set()
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

        return self.productions

    def removeUnit(self):
        for left, right in self.productions.items():
            # In m variant I have no inner loops occurring, so I can just replace the unit productions
            # with the right hand side of the specific production
            for e in right:
                if len(e) == 1 and e in self.nonTerminal:
                    self.productions[left].remove(e)
                    self.productions[left].extend(self.productions[e])
                    self.removeUnit()

        return self.productions

    def removeInaccessible(self):
        reachable = set()
        reachable.add(self.startSymbol)

        while reachable is not None:
            symbol = reachable.pop()
            if symbol not in reachable:
                reachable.add(symbol)
                product = self.productions[symbol]

    def removeNonProductive(self):
        productive = {self.startSymbol}
        old_size = 0
        while len(productive) > old_size:
            old_size = len(productive)
            for left, right in self.productions.items():
                if left in productive:
                    for prod in right:
                        if all(s in productive for s in prod):
                            productive.add(left)
                            break
        self.nonTerminal = [s for s in self.nonTerminal if s in productive]
        self.productions = {left: [prod for prod in right if all(s in productive for s in prod)] for left, right in
                            self.productions.items() if left in productive}

        return self.productions
