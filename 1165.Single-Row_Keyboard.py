class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ord = {c: i for i, c in enumerate(keyboard)}
        return sum(abs(ord[c2]-ord[c1]) for c1, c2 in zip(keyboard[0] + word, word))
