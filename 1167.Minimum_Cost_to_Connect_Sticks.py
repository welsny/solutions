from heapq import heapify, heappop, heappush

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        
        res = 0
        while len(sticks) > 1:
            a, b = heappop(sticks), heappop(sticks)
            res += a+b
            heappush(sticks, a+b)
        return res