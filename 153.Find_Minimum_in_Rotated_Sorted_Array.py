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

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1

        while start < end:
            m = (start+end)//2
            if nums[m] > nums[m+1]: return nums[m+1]
            if nums[m] > nums[start]: start = m
            else: end = m

        return nums[0]

