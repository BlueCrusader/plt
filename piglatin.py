from gettext import translation


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
            #self._translation = self._phrase
            self._translation = ""
            translation_list = self._phrase.split()
            count = 0
            translation_result_list = []
            for x in translation_list:

                translation_word = x

                first_letter = ""
                consonants = (
                'q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q',
                'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')

                while translation_word.startswith(consonants):
                    if translation_word.startswith(consonants):
                        first_letter = translation_word[0]
                        translation_word = translation_word[1:]
                        translation_word = translation_word + first_letter

                vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
                if translation_word.endswith(vowels):
                    translation_word = translation_word + "yay"
                else:
                    if translation_word.endswith('y'):
                        translation_word = translation_word + "nay"
                    else:
                        translation_word = translation_word + "ay"

                self._translation = self._translation + translation_word
                count = count + 1
                if (len(translation_list) != count):
                    self._translation = self._translation + " "



        return self._translation
