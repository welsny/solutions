class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        A = Counter(A.split())
        B = Counter(B.split())
        
        res = []
        
        for word, ct in A.items():
            if ct == 1 and word not in B:
                res.append(word)
        for word, ct in B.items():
            if ct == 1 and word not in A:
                res.append(word)

        return res