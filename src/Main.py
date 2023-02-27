from grammar.Grammar import Grammar
from src.automaton.Transition import Transition


def convert_to_regular_grammar(fa):
    # Create a new start symbol and add an accept rule
    start_symbol = 'S'
    productions = {start_symbol: ['']}
    # Add a rule for each transition
    for state in fa.states:
        for symbol in fa.alphabet:
            next_states = set()
            for transition in fa.transitions:
                if transition.getCurrentState() == state and transition.getTransitionLabel() == symbol:
                    next_states.add(transition.getNextState())
            if next_states:
                # Use a new non-terminal symbol for each combination of state, symbol, and next state
                for next_state in next_states:
                    new_symbol = state + symbol + next_state
                    productions.setdefault(state, []).append(symbol + new_symbol)
                    productions.setdefault(new_symbol, []).append('')
    # Add a rule for each accept state
    for accept_state in fa.acceptStates:
        productions.setdefault(accept_state, []).append('')
    # Create the grammar object
    rg = Grammar(start_symbol, fa.alphabet, list(fa.states), productions)
    return rg




if __name__ == '__main__':
    startingCharacter = 'S'
    nonTerminal = ['S', 'D', 'F']
    terminal = ['a', 'b', 'c', 'd']
    productions = {
        'S': ["aS", "bS", "cD"],
        'D': ["dD", "bF", "a"],
        'F': ["bS", "a"]
    }

    '''
    Lab 1
    ------------------------------------------------
    # Task a
    print("\na) Grammar:")
    print("Non-terminal symbols: ", nonTerminal)
    print("Terminal symbols: ", terminal)
    print("Starting character: ", startingCharacter)
    print("Productions: ", productions)
    grammar = Grammar(startingCharacter, terminal, nonTerminal, productions)

    # Task b
    print("\nb) Generated words:")
    for i in range(5):
        word = grammar.generateWord()
        print(str(i + 1) + '. ' + word)

    # Task c
    finiteAutomaton = grammar.toFiniteAutomaton()
    print("\nc) Finite automaton:")
    print("Alphabet: ", finiteAutomaton.getAlphabet())
    print("States: ", finiteAutomaton.getStates())
    print("Initial state: ", finiteAutomaton.getStartState())
    print("Accepting states: ", finiteAutomaton.getAcceptStates())
    print(finiteAutomaton.getTransitions())

    # Task d
    validWord1 = grammar.generateWord()
    validWord2 = grammar.generateWord()

    print("\nd) Check if a word is valid:")
    print("baca", "-", finiteAutomaton.wordIsValid("baca"))
    print("abcdeee", "-", finiteAutomaton.wordIsValid("abcdeee"))
    print("acdba", "-", finiteAutomaton.wordIsValid("acdba"))
    print("dbbbaacc", "-", finiteAutomaton.wordIsValid("dbbbaacc"))
    print("(Empty)", "-", finiteAutomaton.wordIsValid(""))
    print("010", "-", finiteAutomaton.wordIsValid("010"))
    print(validWord1, "-", finiteAutomaton.wordIsValid(validWord1))
    print("abc1", "-", finiteAutomaton.wordIsValid("abc1"))
    print(validWord2, "-", finiteAutomaton.wordIsValid(validWord2))
    
    '''

    # Check the grammar Type
    grammar = Grammar(startingCharacter, terminal, nonTerminal, productions)
    grammarType = grammar.classifyGrammar()
    print(grammarType)

    finiteAutomaton = grammar.toFiniteAutomaton()

    # Check if Deterministic
    print(finiteAutomaton.isDeterministic())

    # Set the fa
    '''
    finiteAutomaton.set_automaton(states={'q0', 'q1', 'q2', 'q3'},
                                  alphabet=['a', 'b', 'c'],
                                  transitions=[
                                      Transition('q0', 'q0', 'a'),
                                      Transition('q0', 'q1', 'a'),
                                      Transition('q1', 'q2', 'b'),
                                      Transition('q2', 'q3', 'c'),
                                      Transition('q3', 'q3', 'c'),
                                      Transition('q2', 'q2', 'a')
                                  ],
                                  start_state='q0',
                                  accept_states={'q3'})
    '''

    # Conversion from fa to regular grammar
    gr1 = convert_to_regular_grammar(finiteAutomaton)
    print(gr1.terminal)
