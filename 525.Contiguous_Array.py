#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = {0: -1}

        result = 0
        ct = [0, 0]
        for i, num in enumerate(nums):
            ct[num] += 1
            if ct[1] - ct[0] in target:
                result = max(result, i - target[ct[1] - ct[0]])
            target.setdefault(ct[1] - ct[0], i)

        return result

