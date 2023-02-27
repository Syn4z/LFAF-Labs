'''
class FiniteAutomaton:
    def __init__(self, transitions):
        self.states = set()
        self.alphabet = list()
        self.transitions = transitions
        self.startState = None
        self.acceptStates = set()

    def getStates(self):
        return self.states

    def setStates(self, states):
        self.states = states

    def getAlphabet(self):
        return self.alphabet

    def setAlphabet(self, alphabet):
        self.alphabet = alphabet

    def getStartState(self):
        return self.startState

    def setStartState(self, startState):
        self.startState = startState

    def getAcceptStates(self):
        return self.acceptStates

    def setAcceptStates(self, acceptStates):
        self.acceptStates = acceptStates

    def getTransitions(self):
        transition_str = "Transitions:\n"
        for t in self.transitions:
            transition_str += str(t) + "\n"
        return transition_str
    '''


class FiniteAutomaton:
    def __init__(self, states: set, alphabet: list, transitions, startState, acceptStates: set):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.startState = startState
        self.acceptStates = acceptStates

    def getStates(self):
        return self.states

    def setStates(self, states):
        self.states = states

    def getAlphabet(self):
        return self.alphabet

    def setAlphabet(self, alphabet):
        self.alphabet = alphabet

    def getStartState(self):
        return self.startState

    def setStartState(self, startState):
        self.startState = startState

    def getAcceptStates(self):
        return self.acceptStates

    def setAcceptStates(self, acceptStates):
        self.acceptStates = acceptStates

    def getTransitions(self):
        transition_str = "Transitions:\n"
        for t in self.transitions:
            transition_str += str(t) + "\n"
        return transition_str

    def wordIsValid(self, word):
        currentState = self.startState[0]
        for c in word:
            foundTransition = False
            for t in self.transitions:
                if t.getCurrentState() == currentState and t.getTransitionLabel() == c:
                    currentState = t.getNextState()
                    foundTransition = True
                    break
            if not foundTransition:
                return False
        return str(currentState) in self.acceptStates

    def isDeterministic(self):
        for state in self.states:
            transitions = [t for t in self.transitions if t.getCurrentState() == state]
            labels = [t.getTransitionLabel() for t in transitions]
            if len(labels) != len(set(labels)):
                return 'Non-Deterministic'
        return 'Deterministic'

    def convertToRegularGrammar(self):
        nonTerminalVariables = self.states
        terminalVariables = self.alphabet
        startingCharacter = self.startState

        productions = []

        # create productions for each transition
        for state in self.states:
            for t in self.transitions:
                if t.getCurrentState() == state and t.getTransitionLabel() != "e":
                    production = state + "->" + str(t.getTransitionLabel()) + t.getNextState()
                    productions.append(production)

        # create productions for each final state
        for finalState in self.acceptStates:
            production = finalState + "->" + "ε"
            productions.append(production)

        # create the array of Production objects
        productionsArray = []
        for production in productions:
            lhs, rhs = production.split("->")
            productionsArray.append(Production(lhs, rhs))

        # create and return the Grammar object
        return Grammar(nonTerminalVariables, terminalVariables, productionsArray, startingCharacter)

