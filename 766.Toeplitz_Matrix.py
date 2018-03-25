#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        d = {}
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i-j not in d:
                    d[i-j] = val
                if d[i-j] != val:
                    return False
        return True

