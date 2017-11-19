#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])

        def neighs(i, j):
            if i > 0:
                yield i-1, j
            if i < m - 1:
                yield i+1, j
            if j > 0:
                yield i, j-1
            if j < n - 1:
                yield i, j+1

        def bfs(s):
            """ In-place add flowable nodes to the set 's' """
            dq = deque(s)
            while len(dq):
                i, j = dq.popleft()
                for a, b in neighs(i, j):
                    if matrix[i][j] <= matrix[a][b] and (a, b) not in s:
                        s.add((a, b))
                        dq.append((a, b))

        pacific = set((i, 0) for i in range(m))
        pacific.update((0, j) for j in range(n))
        bfs(pacific)

        atlantic = set((i, n-1) for i in range(m))
        atlantic.update((m-1, j) for j in range(n))
        bfs(atlantic)

        return list(pacific & atlantic)

