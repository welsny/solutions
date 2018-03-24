#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cts = Counter(nums)
        for num, ct in cts.items():
            if ct > len(nums)//2:
                return num

