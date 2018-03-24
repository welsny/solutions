#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cts = Counter(nums)
        return max((ct + cts[n+1] for n, ct in cts.items() if n+1 in cts), default=0)

