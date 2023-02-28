class FiniteAutomaton:
    def __init__(self, states: set, alphabet: list, transitions: list, startState, acceptStates: set):
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
        return self.transitions

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
            transitions = [t for t in self.transitions if t[0] == state]
            labels = [t[1] for t in transitions]
            if len(labels) != len(set(labels)):
                return 'Non-Deterministic'
        return 'Deterministic'

    '''
    def convertToRegularGrammar(self, Grammar):
        nonTerminalVariables = self.states
        terminalVariables = self.alphabet
        startingCharacter = self.startState

        productions = []

        # create productions for each transition
        for state in self.states:
            for t in self.transitions:
                if t[0] == state and t[1] != "e":
                    production = state + "->" + str(t[1]) + "->" + t[2]
                    productions.append(production)

        # create productions for each final state
        for finalState in self.acceptStates:
            production = finalState + "->" "ε"
            productions.append(production)

        # create and return the Grammar object
        return Grammar(startingCharacter, terminalVariables, nonTerminalVariables, productions)
    '''

    def convertToRegularGrammar(self, Grammar):
        productions = {}

        # Step 1: Add a new start symbol S
        startSymbol = self.startState
        productions[startSymbol] = [self.startState]

        # Step 2: Create a new non-terminal symbol for each state
        for state in self.states:
            productions[state] = []

        # Step 3: Add production rules for accept states
        for acceptState in self.acceptStates:
            for state in self.states:
                if acceptState == state:
                    productions[state].append("ε")

        # Step 4: Add production rules for transitions
        for transition in self.transitions:
            q, a, p = transition
            productions[q].append(a + p)

        # Create Grammar object
        nonTerminal = list(self.states)
        terminal = self.alphabet
        return Grammar(startSymbol, terminal, nonTerminal, productions)

    def convertToDFA(self):
        # First, create a set of all possible combinations of NFA states
        powerSet = self.getPowerSet(self.states)

        # Initialize the new DFA
        dfaStates = set()
        dfaTransitions = []
        dfaStartState = self.startState
        dfaAcceptStates = set()

        # Process each set of NFA states in the power set
        for stateSet in powerSet:
            stateSet = frozenset(stateSet)  # convert frozenset to set
            dfaStates.add(stateSet)

            # Determine the set of possible transitions for this set of states
            transitions = {}
            for state in stateSet:
                if state in self.transitions:
                    for transition in self.transitions[state]:
                        if transition[0] in self.alphabet:
                            if transition[0] not in transitions:
                                transitions[transition[0]] = set()
                            transitions[transition[0]].add(transition[1])

            # Add the transitions for this DFA state
            for symbol in self.alphabet:
                if symbol in transitions:
                    nextStateSet = frozenset(transitions[symbol])
                    if nextStateSet not in dfaStates:
                        dfaStates.add(nextStateSet)
                    dfaTransitions.append((stateSet, symbol, nextStateSet))

            # Check if this set of NFA states contains any accept states
            for acceptState in self.acceptStates:
                if acceptState in stateSet:
                    dfaAcceptStates.add(stateSet)

        # Create the new DFA object and return it
        dfa = FiniteAutomaton(dfaStates, self.alphabet, dfaTransitions, dfaStartState, dfaAcceptStates)
        return dfa

    def getPowerSet(self, originalSet):
        # Helper function to generate the power set of a set
        if len(originalSet) == 0:
            return [[]]
        else:
            element = originalSet.pop()
            powerSet = self.getPowerSet(originalSet)
            newSet = []
            for subset in powerSet:
                newSet.append(subset)
                newSubset = subset.copy()
                newSubset.append(element)
                newSet.append(newSubset)
            return newSet
