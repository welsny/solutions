#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)

        result = 0
        targets = defaultdict(int)
        for n in sums:
            if n in targets:
                result += targets[n]
            targets[k+n] += 1
        return result

