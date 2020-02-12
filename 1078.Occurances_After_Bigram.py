class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        words = text.split()
        for i, word in enumerate(words[:-2]):
            word2, word3 = words[i+1:i+3]
            if word == first and word2 == second:
                res.append(word3)
        return res