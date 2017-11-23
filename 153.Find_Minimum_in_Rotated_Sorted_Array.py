#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        if nums[start] < nums[end]:
            return nums[start]

        while end - start > 1:
            mid = (start + end)//2
            if nums[mid] < nums[start]:
                end = mid
            else:
                start = mid

        return nums[end]

