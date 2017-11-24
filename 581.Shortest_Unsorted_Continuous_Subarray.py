#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: This was an accepted nLogn solution -- there is a linear time solution though.

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        srt = sorted(nums)
        diff = [i for i, (n, m) in enumerate(zip(nums, srt)) if n != m]
        return max(diff) - min(diff) + 1 if diff else 0

