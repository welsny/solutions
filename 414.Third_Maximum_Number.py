#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = heapq.nlargest(3, set(nums))
        return res[-1] if len(res) >= 3 else res[0]

