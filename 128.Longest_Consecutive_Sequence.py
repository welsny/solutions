#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        max = 0
        curr = 0
        while nums:
            i = nums.pop()
            curr += 1

            up = i+1
            while up in nums:
                nums.remove(up)
                up += 1
                curr += 1

            down = i-1
            while down in nums:
                nums.remove(down)
                down -= 1
                curr += 1

            if curr > max:
                max = curr
            curr = 0

        return max
