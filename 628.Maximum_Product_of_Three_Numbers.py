#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
import operator
from functools import reduce

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return reduce(operator.mul, nums)

        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i <= 0]
        sols = []

        if len(pos) >= 3:
            sols.append(reduce(operator.mul, heapq.nlargest(3, pos)))
        if pos and len(neg) >= 2:
            sols.append(max(pos) * reduce(operator.mul, heapq.nsmallest(2, neg)))
        if not pos:
            sols.append(reduce(operator.mul(heapq.nlargest(3, neg))))

        return max(sols)

import heapq

class Solution:
    def maximumProduct(self, nums):
        """
        Improved solution. In my original solution, I overcomplicated things by separating things into positive and negative. I think in an interview, it would make sense to present this solution first and then run test cases for edge cases instead of explaining it from a mathematical proof perspective.

        :type nums: List[int]
        :rtype: int
        """
        h, l = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(h[0] * h[1] * h[0], h[0] * l[0] * l[1])


