#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        maxs = {}
        for i, value in enumerate(nums):
            maxs[i] = max(value + maxs.get(i-2, 0), maxs.get(i-1, 0))

        return maxs[len(nums)-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        More concise solution that uses less memory:

        O(N) Time
        O(1) Space
        """
        prev = curr = 0
        for n in nums:
            prev, curr = curr, max(n+prev, curr)
        return curr
