import unittest
from buzz import generator

class TestGenerator(unittest.TestCase):

    def test_sample_single_word(self):
        l = ('foo', 'bar', 'foobar')
        word = generator.sample(l)
        self.assertIn(word, l)

    def test_sample_multiple_words(self):
        l = ('foo', 'bar', 'foobar')
        words = generator.sample(l, 2)
        self.assertEqual(len(words), 2)
        self.assertIn(words[0], l)
        self.assertIn(words[1], l)
        self.assertNotEqual(words[0], words[1])

    def test_generate_buzz_of_at_least_five_words(self):
        phrase = generator.generate_buzz()
        self.assertGreaterEqual(len(phrase.split()), 5)

if __name__ == '__main__':
    unittest.main()
