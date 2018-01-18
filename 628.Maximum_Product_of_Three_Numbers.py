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

