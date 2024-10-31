class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase
        self._translation = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if (not (self._phrase and self._phrase.strip())):
            self._translation = "nil"


        return self._translation
