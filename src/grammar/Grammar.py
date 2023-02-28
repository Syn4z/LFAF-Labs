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

    def generateWordHelper(self, character: str) -> str:
        if character in self.terminal:
            return character
        rightSide = self.productions[character]
        randomRightSide = random.choice(rightSide)
        word = ''
        for rightChar in randomRightSide:
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
                if len(production) > 2 or (production[0] not in self.terminal and production[0] not in self.nonTerminal) \
                        or (len(production) == 2 and production[1] not in self.nonTerminal):
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
