#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def moveZeroes(self, nums):
        """
        My first accepted solution.

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

class Solution:
    def moveZeroes(self, nums):
        """
        New and improved solution:

        We actually didn't need to do the first pass when we count the number of non-zero elements. Instead, we swap elements when we find non-zero elements. This allows us to move non-zero elements to the start of the list. Note this allows us to preserve the array's contents in each iteration of the loop.

        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pt = 0 # Pointer next position for non-zero entries:

        for i, num in enumerate(nums):
            if num:
                nums[i], nums[pt] = nums[pt], nums[i]
                pt += 1


