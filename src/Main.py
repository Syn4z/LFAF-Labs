from src.grammar.Grammar import Grammar

if __name__ == '__main__':

    grammar = Grammar(
        'S', ['a', 'b', 'd'], ['S', 'A', 'B', 'C', 'D'], {'S': ['dB', 'AC'],
                                                          'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC'], 'D': ['ab'],
                                                          'C': ['bC', 'ε']})

    print(grammar.toChomskyNormalForm())
