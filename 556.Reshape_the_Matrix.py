#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n, m = len(nums), len(nums[0])
        if r*c != n*m:
            return nums

        result = [[None for i in range(c)] for j in range(r)]

        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                ct = i * m + j
                result[ct//c][ct%c] = num

        return result
