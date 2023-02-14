from src.automaton.FiniteAutomaton import FiniteAutomaton
import random


class Grammar:

    def __init__(self, startingChar, productions):
        self.productions = productions
        self.startingChar = startingChar

    def generateWord(self):
        stack = [self.startingChar]
        result = []
        while stack:
            top = stack.pop()
            production = random.choice([p for p in self.productions if p.leftSide == top])
            for symbol in reversed(production.rightSide):
                if symbol not in self.productions:
                    result.append(symbol)
                else:
                    stack.append(symbol)
        return result

    def toFiniteAutomaton(self):
        states = []
        initial_state = (self.startingChar, 0)
        final_states = []
        transitions = []

        def closure(state):
            nonlocal states, transitions
            if state not in states:
                states.append(state)
                symbol, position = state
                if position < len(symbol):
                    for production in self.productions:
                        if symbol[position] == production.leftSide:
                            for right in production.rightSide:
                                transitions.append((state, (right, 0)))
                                closure((right, 0))

        closure(initial_state)
        for state in states:
            symbol, position = state
            if position == len(symbol):
                final_states.append(state)

        return FiniteAutomaton(states, initial_state, final_states, transitions)
