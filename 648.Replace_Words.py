class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        res = []
        d = set(dict)

        for word in sentence.split():
            for i, _ in enumerate(word):
                if word[:i] in d:
                    res.append(word[:i])
                    break
            else:
                res.append(word)

        return " ".join(res)
