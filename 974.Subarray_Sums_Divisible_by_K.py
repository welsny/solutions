from collections import defaultdict

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        cts = defaultdict(int)
        cts[0] = 1
        curr = 0
        for a in A:
            curr += a
            curr %= K
            res += cts[curr]
            cts[curr] += 1

        return res