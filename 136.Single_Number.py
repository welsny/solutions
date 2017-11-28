#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [num for num, ct in Counter(nums).items() if ct%2][0]

