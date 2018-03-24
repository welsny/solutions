#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        labels = {}
        for rank, num in enumerate(sorted(nums, reverse=True)):
            if rank == 0:
                labels[num] = 'Gold Medal'
            elif rank == 1:
                labels[num] = 'Silver Medal'
            elif rank == 2:
                labels[num] = 'Bronze Medal'
            else:
                labels[num] = str(rank+1)
        return [labels[num] for num in nums]

