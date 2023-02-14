from grammar.Grammar import Grammar
from grammar.Production import Production
from automaton.FiniteAutomaton import FiniteAutomaton

"""
class Main: {

}
"""

if __name__ == '__main__':
    pass

    # VN = ["S", "D", "F"]
    # VT = ["a", "b", "c", "d"]
    # P = Production(["S", "D", "F"], ["aS", "bS", "cD", "dD", "bF", "a", "bs", "a"])

    grammar = Grammar("S", [
        Production("S", ["aS", "bS", "cD"]),
        Production("D", ["dD", "bF", "a"]),
        Production("F", ["bS", "a"])
    ])

    # Generate a word from the grammar.
    word = "-> ".join(grammar.generateWord())
    print(word)


    automaton = FiniteAutomaton(
        possibleStates=[("S", 0), ("A", 0), ("B", 0), ("C", 0), ("a", 1), ("b", 1), ("c", 1), ("d", 1), ("e", 1), ("f", 1)],
        initialState=("S", 0),
        finalState=[("a", 1), ("b", 1), ("c", 1), ("d", 1), ("e", 1), ("f", 1)],
        transitions=[
            (("S", 0), ("A", 0)),
            (("S", 0), ("B", 0)),
            (("S", 0), ("C", 0)),
            (("A", 0), ("a", 1)),
            (("A", 0), ("b", 1)),
            (("B", 0), ("c", 1)),
            (("B", 0), ("d", 1)),
            (("C", 0), ("e", 1)),
            (("C", 0), ("f", 1)),
        ],
    )

    # Verify if a word is valid.
    word = "f"
    valid = automaton.isValid(word)
    print(f"The word '{word}' is valid: {valid}")

    word = "abcdef"
    valid = automaton.isValid(word)
    print(f"The word '{word}' is valid: {valid}")
