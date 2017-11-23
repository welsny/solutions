#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        if numRows >= 1:
            result.append([1])
        if numRows >= 2:
            result.append([1, 1])
        if numRows >= 3:
            for i in range(3, numRows+1):
                result.append([1] + [k+result[-1][i+1] for i, k in enumerate(result[-1]) if i < len(result[-1])-1] + [1])

        return result
