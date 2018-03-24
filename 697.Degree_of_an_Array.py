#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        ind = {}

        for i, num in enumerate(nums):
            freq[num] += 1

            if num not in ind:
                ind[num] = [i, i]
            else:
                ind[num][1] = i

        return min(l-f+1 for num, (f, l) in ind.items() if freq[num] == max(freq.values())) if nums else 0

