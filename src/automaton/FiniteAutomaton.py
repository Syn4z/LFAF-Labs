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

    def epsilon_closure(self, states, transitions):
        e_closure = set(states)
        queue = list(states)
        while queue:
            state = queue.pop(0)
            for transition in transitions:
                if transition[0] == state and transition[1] == 'ε':  # epsilon transition
                    if transition[2] not in e_closure:
                        e_closure.add(transition[2])
                        queue.append(transition[2])
        return e_closure

    def move(self, states, symbol, transitions):
        next_states = set()
        for state in states:
            for transition in transitions:
                if transition[0] == state and transition[1] == symbol:
                    next_states.add(transition[2])
        return next_states

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

    def convertNFAtoDFA(self):
        # Initialize variables
        dfa_states = set()
        dfa_alphabet = self.alphabet
        dfa_transitions = []
        dfa_startState = frozenset(self.epsilon_closure({self.startState}, self.transitions))
        dfa_acceptStates = set()

        queue = [dfa_startState]
        processed_states = set()

        # Loop until there are no more states to visit
        while queue:
            state_set = queue.pop(0)
            if state_set in processed_states:
                continue
            processed_states.add(state_set)

            # Add the current state set to the DFA states
            dfa_states.add(state_set)

            # Check if the current state set contains an accept state from the NDFA
            for accept_state in self.acceptStates:
                if accept_state in state_set:
                    dfa_acceptStates.add(state_set)
                    break

            # Calculate transitions for the current state set
            for symbol in dfa_alphabet:
                next_states = self.epsilon_closure(self.move(state_set, symbol, self.transitions), self.transitions)
                if len(next_states) > 0:
                    dfa_transitions.append((state_set, symbol, frozenset(next_states)))
                    if frozenset(next_states) not in processed_states:
                        queue.append(frozenset(next_states))

        # Create the DFA object
        dfa = FiniteAutomaton(states=dfa_states,
                              alphabet=dfa_alphabet,
                              transitions=dfa_transitions,
                              startState=dfa_startState,
                              acceptStates=dfa_acceptStates)
        return dfa

