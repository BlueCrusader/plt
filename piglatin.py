from gettext import translation
from string import punctuation


class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase
        self._translation = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not (self._phrase and self._phrase.strip()):
            self._translation = "nil"
        else:
            punctuations = ('.', ',', ';', ':', '’', '?', '!', '(', ')', '!', '!', '!', '!', '!')
            punctuation = ""

            self._translation = self._phrase
            translation_phrase = self._translation

            if self._translation.endswith(punctuations):
            #    punctuation = self._translation[-1]
                N = 1
                lengthA = len(self._translation)
                punctuation = self._translation[lengthA - N:]
            #    translation_phrase = self._translation[:1]
                translation_phrase = translation_phrase[:len(translation_phrase) - 1]
            else:
                translation_phrase = self._translation



            self._translation = ""
            #translation_list = self._phrase.split()
            translation_list = translation_phrase.split()


            count = 0

            translation_result_list = []
            for x in translation_list:

                translation_word = x
                split_translation_word_list = translation_word.split("-")

                translation_word = ""
                countB = 0

                for y in split_translation_word_list:


                    split_word = y

                    first_letter = ""
                    consonants = (
                        'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n',
                        'm', 'Q',
                        'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')

                    while split_word.startswith(consonants):
                        if split_word.startswith(consonants):
                            first_letter = split_word[0]
                            split_word = split_word[1:]
                            split_word = split_word + first_letter

                    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
                    if split_word.endswith(vowels):
                        split_word = split_word + "yay"
                    else:
                        if split_word.endswith('y'):
                            split_word = split_word + "nay"
                        else:
                            split_word = split_word + "ay"



                    translation_word = translation_word + split_word
                    countB = countB + 1
                    if (len(split_translation_word_list) != countB):
                        translation_word = translation_word + "-"


                self._translation = self._translation + translation_word
                count = count + 1
                if (len(translation_list) != count):
                    self._translation = self._translation + " "


            self._translation = self._translation + punctuation

        return self._translation
