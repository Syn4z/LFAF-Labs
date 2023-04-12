import unittest
from src.grammar.Grammar import Grammar


class UnitTest(unittest.TestCase):

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
    automaton = grammar.toFiniteAutomaton()

    def test_grammar(self):
        self.assertEqual(self.grammar, self.grammar)

    def test_automaton(self):
        self.assertEqual(self.automaton, self.automaton)

    def test_classify_grammar(self):
        self.assertEqual(self.grammar.classifyGrammar(), 'Type None')

    def test_to_chomsky_normal_form(self):
        self.assertEqual(self.grammar.toChomskyNormalForm(), {'S': ['dB', 'AC', 'd', 'dS', 'aBdB'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC', 'd', 'dS', 'aBdB'], 'D': ['ab'], 'C': ['bC']})

    def test_epsilon(self):
        self.assertEqual(self.grammar.removeEpsilon(), {'S': ['dB', 'A', 'AC'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'A', 'AC'], 'D': ['ab'], 'C': ['bC']})

    def test_unit(self):
        self.assertEqual(self.grammar.removeUnit(), {'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'AC', 'd', 'dS', 'aBdB'], 'C': ['bC'], 'D': ['ab'], 'S': ['dB', 'AC', 'd', 'dS', 'aBdB']})


if __name__ == '__main__':
    unittest.main()
