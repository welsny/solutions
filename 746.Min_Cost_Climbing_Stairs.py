#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i, c in enumerate(cost):
            if i >= 2:
                cost[i] = c + min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])

