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

            vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y')
            if self._phrase.endswith(vowels):
                if self._phrase.endswith('y'):
                    self._translation = self._translation + "nay"
                else:
                 self._translation = self._translation + "yay"
            else:
                self._translation = self._translation + "ay"

        return self._translation
