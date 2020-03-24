#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A: return 0

        maxs = defaultdict(lambda: float('-inf'))
        maxs[0, 0] = A[0][0]

        n, m = len(A), len(A[0])
        def adjs(score, i, j):
            res = []
            for x, y in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= x < n and 0 <= y < m:
                    s = min(score, A[x][y])
                    if s > maxs[x, y]:
                        res.append((s, x, y))

            return res

        heap = [(-A[0][0], 0, 0)]
        while heap:
            score, i, j = heappop(heap)

            score = -score
            for s, x, y in adjs(score, i, j):
                if x == n-1 and y == m-1:
                    return s
                maxs[x, y] = s
                heappush(heap, (-s, x, y))
