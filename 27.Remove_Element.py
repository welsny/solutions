#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def removeElement(self, nums, val):
        """
        The solution is based on the same concept as #283.

        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pt = 0

        for i, num in enumerate(nums):
            if num != val:
                nums[i], nums[pt] = nums[pt], nums[i]
                pt += 1
        return pt

