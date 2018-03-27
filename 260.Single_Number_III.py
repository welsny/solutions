#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ct = Counter(nums)
        return [n for n, ct in ct.items() if ct == 1]

