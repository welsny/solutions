#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ct = sum(1 for i in nums if i)

        pt = 0 # Pointer to next non-zero element
        for i, num in enumerate(nums):
            if i < ct:
                while not nums[pt]:
                    pt += 1
                nums[i] = nums[pt]
                pt += 1
            else:
                nums[i] = 0

