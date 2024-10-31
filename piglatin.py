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
            self._translation = self._phrase
            first_letter = ""
            consonants = ('q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'R', 'T', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M')
            #if self._phrase.startswith(consonants):
            #    first_letter = self._phrase[0]
            #    self._translation = self._translation[1:]
            #    self._translation = self._translation + first_letter

            while self._translation.startswith(consonants):
                if self._translation.startswith(consonants):
                    first_letter = self._translation[0]
                    self._translation = self._translation[1:]
                    self._translation = self._translation + first_letter


            vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
            if self._translation.endswith(vowels):
                 self._translation = self._translation + "yay"
            else:
                if self._phrase.endswith('y'):
                    self._translation = self._translation + "nay"
                else:
                    self._translation = self._translation + "ay"

        return self._translation
