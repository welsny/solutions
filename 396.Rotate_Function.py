#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n, s = len(A), sum(A)
        result = f = sum(i*j for i, j in zip(range(n), A))

        for i in range(n):
            f += s - n*A[-i-1]
            result = max(result, f)

        return result

