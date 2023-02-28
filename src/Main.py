import random

import graphviz
from grammar.Grammar import Grammar
from src.automaton.FiniteAutomaton import FiniteAutomaton

if __name__ == '__main__':
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

    startingCharacter = 'S'
    nonTerminal = ['S', 'D', 'F']
    terminal = ['a', 'b', 'c', 'd']
    productions = {
        'S': ["aS", "bS", "cD"],
        'D': ["dD", "bF", "a"],
        'F': ["bS", "a"]
    }

    # Check the grammar Type, 2a
    grammar = Grammar(startingCharacter, terminal, nonTerminal, productions)
    grammarType = grammar.classifyGrammar()
    print("2a) Grammar Type: \n", grammarType)

    # Conversion from FA to regular grammar
    gr1 = FiniteAutomaton(states={'q0', 'q1', 'q2', 'q3'},
                          alphabet=['a', 'b', 'c'],
                          transitions=[
                              ('q0', 'a', 'q0'),
                              ('q0', 'a', 'q1'),
                              ('q1', 'b', 'q2'),
                              ('q2', 'c', 'q3'),
                              ('q3', 'c', 'q3'),
                              ('q2', 'a', 'q2')
                          ],
                          startState='q0',
                          acceptStates={'q3'})

    # Function to classify the grammar based on Chomsky hierarchy, 3a
    gr2 = gr1.convertToRegularGrammar(Grammar)
    print("\n3a) Regular Grammar converted from FA:")

    print("\nFinite automaton:")
    print("Alphabet: ", gr1.getAlphabet())
    print("States: ", gr1.getStates())
    print("Initial state: ", gr1.getStartState())
    print("Accepting states: ", gr1.getAcceptStates())
    print("Transitions: ", gr1.getTransitions())

    print("\nRegular Grammar:")
    print("NonTerminal symbols: ", gr2.nonTerminal)
    print("Terminal symbols: ", gr2.terminal)
    print("Starting character: ", gr2.startSymbol)
    print("Productions: ", gr2.productions)


    gr2.generateWord()

    # Check if Deterministic, 3b
    print("\n3b) IsDeterministic? \n", gr1.isDeterministic())

    # Convert NDFA to DFA, 3c
    dfa = gr1.convertToDFA()

    print("Alphabet: ", dfa.getAlphabet())
    print("States: ", dfa.getStates())
    print("Initial state: ", dfa.getStartState())
    print("Accepting states: ", dfa.getAcceptStates())
    print("Transitions: ", dfa.getTransitions())

    print(dfa.isDeterministic())

    # Represent the finite automaton graphically, 3d
    graph = graphviz.Digraph()

    # Add the states and transitions to the graph
    for state in gr1.getStates():
        shape = 'circle' if state not in gr1.getAcceptStates() else 'doublecircle'
        graph.node(state, shape=shape)
    for (from_state, symbol, to_state) in gr1.getTransitions():
        graph.edge(from_state, to_state, label=symbol)

    # Set the start state of the DFA
    graph.node('', shape='none', label='', width='0')
    graph.edge('', gr1.getStartState())

    # Save the graph as a PDF file
    graph.render('dfa', view=True)
