import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_input(self):
        translator = PigLatin("Hello World")
        phrase = translator.get_phrase()
        # translation = translator.translate()
        self.assertEqual( "Hello World", phrase)

    def test_translator_empty_input(self):
        translator = PigLatin("")
        #phrase = translator.get_phrase()
        translation = translator.translate()
        self.assertEqual( "nil", translation)

    def test_translator_input_ending_with_y(self):
        translator = PigLatin("any")
        #phrase = translator.get_phrase()
        translation = translator.translate()
        self.assertEqual( "anynay", translation)

    def test_translator_input_ending_with_other_vowel(self):
        translator = PigLatin("apple")
        #phrase = translator.get_phrase()
        translation = translator.translate()
        self.assertEqual( "appleyay", translation)

    def test_translator_input_ending_with_consonant(self):
        translator = PigLatin("ask")
        #phrase = translator.get_phrase()
        translation = translator.translate()
        self.assertEqual( "askay", translation)

