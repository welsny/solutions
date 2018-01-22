#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1] + [0] * n

        if n >= 1:
            steps[1] = 1

        for i in range(n+1):
            if i >= 2:
                steps[i] = steps[i-2] + steps[i-1]

        return steps[-1]

