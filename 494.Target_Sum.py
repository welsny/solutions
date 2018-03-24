#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        cts = {0: 1}

        for n in nums:
            next_cts = defaultdict(int)
            for part_sum, ct in cts.items():
                next_cts[part_sum + n] += ct
                next_cts[part_sum - n] += ct
            cts = next_cts

        return cts[S]

