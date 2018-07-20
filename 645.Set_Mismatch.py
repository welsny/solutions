#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cts = Counter(nums)

        target = len(nums) * (len(nums) + 1) // 2

        for n, ct in cts.items():
            if ct == 2:
                return [n, target - sum(cts.keys())]

