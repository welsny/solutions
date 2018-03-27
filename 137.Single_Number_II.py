#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cts = Counter(nums)
        return [n for n, ct in cts.items() if ct == 1][0]

