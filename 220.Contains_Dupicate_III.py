#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        seen = {}

        for i, value in enumerate(nums):
            for s in seen:
                if abs(s-value) <= t and i - seen[s] <=k:
                    return True
            seen[value] = i

        return False

