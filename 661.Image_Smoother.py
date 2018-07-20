#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor

class Solution(object):

    def neighbors(self, i, j):
        result = []

        for a in [i-1, i, i+1]:
            for b in [j-1, j, j+1]:
                if 0 <= a < self.rows and 0 <= b < self.cols:
                    result.append(self.M[a][b])

        return result

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        self.M = M
        self.rows = len(M)
        self.cols = len(M[0])

        result = [[None for i in range(self.cols)] for j in range(self.rows)]

        for i, row in enumerate(M):
            for j, _ in enumerate(row):
                n = self.neighbors(i, j)
                result[i][j] = int(math.floor(sum(n)/len(n)))

        return result

