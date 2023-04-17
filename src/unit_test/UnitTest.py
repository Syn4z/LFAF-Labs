import unittest
from src.grammar.Grammar import Grammar
import src.automaton.FiniteAutomaton as FiniteAutomaton


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

    def test_generateWord(self):
        self.assertEqual(self.grammar.generateWord(), self.grammar.generateWord())

    def test_classify_grammar(self):
        self.assertEqual(self.grammar.classifyGrammar(), 'Type None')

    def test_automaton(self):
        self.assertEqual(self.automaton, self.automaton)

    def test_deterministic(self):
        self.assertEqual(self.automaton.isDeterministic(), "Non-Deterministic")

    def test_convertFaToGrammar(self):
        self.assertEqual(self.automaton.convertToRegularGrammar(Grammar), ({'S': ['dB', 'AC'],
                                                                            'A': ['d', 'dS', 'aBdB'],
                                                                            'B': ['a', 'aA', 'AC'],
                                                                            'D': ['ab'],
                                                                            'C': ['bC', 'ε']},
                                                                           ['a', 'b', 'd'],
                                                                           ['S', 'A', 'B', 'C', 'D']))

    def test_nfaToDfa(self):
        self.assertEqual(self.automaton.convertNFAtoDFA(), ({'S': {'a': 'A', 'd': 'B'},
                                                             'A': {'a': 'A', 'd': 'B'},
                                                             'B': {'a': 'A', 'd': 'B'}},
                                                            ['a', 'd'],
                                                            ['S', 'A', 'B']))

    def test_wordValid(self):
        self.assertEqual(self.automaton.wordIsValid("dad"), True)

    def test_to_chomsky_normal_form(self):
        self.assertEqual(self.grammar.toChomskyNormalForm(), ({'A': ['d', 'S', 'a'],
                                                               'B': ['a', 'A', 'd', 'S'],
                                                               'S': ['B', 'A', 'd', 'S', 'a']},
                                                              ['a', 'b', 'd'],
                                                              ['S', 'A', 'B']))

    def test_epsilon(self):
        self.assertEqual(self.grammar.removeEpsilon(),
                         {'S': ['dB', 'A', 'AC'], 'A': ['d', 'dS', 'aBdB'], 'B': ['a', 'aA', 'A', 'AC'], 'D': ['ab'],
                          'C': ['bC']})


if __name__ == '__main__':
    unittest.main()
