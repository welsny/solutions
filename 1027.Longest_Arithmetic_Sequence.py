from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        prevs = set()
        seq = defaultdict(
            lambda: defaultdict(int)
        )
        res = 0
        for a in A:
            for p in prevs:
                seq[a][a-p] = max(seq[a][a-p], (a == p and 1) or 2)
                res = max(res, 2)
            for p, deltas in seq.items():
                if a-p in deltas:
                    seq[a][a-p] = deltas[a-p] + 1
                    res = max(res, seq[a][a-p])
            prevs.add(a)
        return res
