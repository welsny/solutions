class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import defaultdict
        cts = defaultdict(int)
        result = 0
        
        for t in time:
            result += cts[(60 - t)%60]
            cts[t % 60] += 1

        return result