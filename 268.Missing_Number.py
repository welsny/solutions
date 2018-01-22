#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums)**2 + len(nums))//2 - sum(nums)

