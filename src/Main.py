from src.grammar.Grammar import Grammar

if __name__ == '__main__':

    startingCharacter = 'S'
    nonTerminal = ['S', 'A', 'B', 'C', 'D']
    terminal = ['a', 'b', 'd']
    productions = {'S': ['dB', 'AC'],
                   'A': ['d', 'dS', 'aBdB'],
                   'B': ['a', 'aA', 'AC'],
                   'D': ['ab'],
                   'C': ['bC', 'ε']
                   }

    grammar = Grammar(startingCharacter, terminal, nonTerminal, productions)

    print("Initial productions:", grammar.productions)
    print("Chomsky Normal Form:", grammar.toChomskyNormalForm())
