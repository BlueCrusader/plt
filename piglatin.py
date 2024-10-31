class PigLatin:

    def __init__(self, phrase: str):
        self._phrase = phrase
        self._translation = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        return self._translation
