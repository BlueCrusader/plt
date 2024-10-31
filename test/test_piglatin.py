import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_translator_input(self):
        translator = PigLatin("Hello World")
        phrase = translator.get_phrase()
        # translation = translator.translate()
        self.assertEqual( "Hello World", phrase)

