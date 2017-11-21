#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cts = [1, 1] + [0]*(n-1)

        for i, ct in enumerate(cts):
            if not ct:
                for j in range(i):
                    cts[i] += cts[j] * cts[i-1-j]

        return cts[-1]

