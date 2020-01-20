class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        ct = Counter(text)
        return min(ct['a'], ct['b'], ct['n'], ct['l']//2, ct['o']//2)