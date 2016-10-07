#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0

        for i in nums:
            if not i:
                red += 1
            elif i == 1:
                white += 1

        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red -= 1
            elif white:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
