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

    print("\tInitial Grammar: " + "\nTerminal: ", grammar.terminal, "\nNon-terminal: ", grammar.nonTerminal,
          "\nProductions: ", grammar.productions)
    grammar.toChomskyNormalForm()
    print("\n\tChomsky Normal Form:" + "\nTerminal: ", grammar.terminal, "\nNon-terminal: ", grammar.nonTerminal,
          "\nProductions: ", grammar.productions)
