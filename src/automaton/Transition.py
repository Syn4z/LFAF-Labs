class Transition:
    def __init__(self, currentState, nextState, transitionLabel):
        self.currentState = currentState
        self.nextState = nextState
        self.transitionLabel = transitionLabel

    def getCurrentState(self):
        return self.currentState

    def getNextState(self):
        return self.nextState

    def getTransitionLabel(self):
        return self.transitionLabel

    def __str__(self):
        return str(self.nextState)
