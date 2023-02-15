from src.automaton.FiniteAutomaton import FiniteAutomaton
from src.automaton.Transition import Transition
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
                transitions.append(Transition(nonTerminal, nextState, transitionLabel))
        automaton = FiniteAutomaton(transitions)
        states.add('X')
        automaton.setStates(states)
        automaton.setStartState(str(self.startSymbol))
        automaton.setAcceptStates(finalStates)
        automaton.setAlphabet(self.terminal)
        return automaton
