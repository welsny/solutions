#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        result = set()
        seen = set()
        for n in nums:
            if n+k in seen:
                result.add((n, n+k))
            if n-k in seen:
                result.add((n-k, n))
            seen.add(n)

        return len(result)

