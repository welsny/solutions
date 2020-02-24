from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return all(ct == 1 for ct in Counter(Counter(arr).values()).values())