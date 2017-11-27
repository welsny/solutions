#!
from collections import defaultdict

class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        prob = defaultdict(int)
        prob[(r, c)] = 1

        for _ in range(K):
            next = defaultdict(int)
            for (r, c), p in prob.items():
                for x, y in self.adj(N, r, c):
                    next[(x, y)] += p/8
            prob = next
        return sum(prob.values())

    def adj(self, N, r, c):
        return ((x, y) for x, y in [(r+2, c+1), (r+2, c-1), (r+1, c+2), (r+1, c-2),
                                    (r-2, c+1), (r-2, c-1), (r-1, c+2), (r-1, c-2)]
                if 0 <= x < N and 0 <= y < N)

