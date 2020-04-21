#!/usr/bin/env python3

from collections import defaultdict, deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        shortest = defaultdict(lambda: float('inf'))

        n = len(grid)
        def adjs(i, j, d):
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1),
                         (i, j-1), (i, j+1),
                         (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if 0 <= x < n and 0 <= y < n and not grid[x][y] and d+1 < shortest[x, y]:
                    yield x, y

        dq = deque([(0, 0, 1)])
        shortest[0, 0] = 1
        while dq:
            i, j, d = dq.popleft()

            if i == j == n-1:
                return d

            for x, y in adjs(i, j, d):
                shortest[x, y] = d+1
                dq.append((x, y, d+1))

        return -1
