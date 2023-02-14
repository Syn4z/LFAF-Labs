class FiniteAutomaton:

    def __init__(self, possibleStates, initialState, finalState, transitions):
        self.possibleStates = possibleStates
        self.transitions = transitions
        self.initialState = initialState
        self.finalState = finalState

    # Function wordIsValid()    TO DO
    def isValid(self, word):
        state = self.initialState
        for symbol in word:
            next_states = [t[1] for t in self.transitions if t[0] == state and t[1][0] == symbol]
            if not next_states:
                return False
            state = next_states[0]
        return state in self.finalState
