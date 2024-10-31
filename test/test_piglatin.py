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

