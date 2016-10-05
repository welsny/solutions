#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums, position=0, last=None):
        """
        :type nums: List[int]
        :rtype: int
        """

        last = None
        uniq = 0

        for e in nums:
            if last is None or e != last:
                nums[uniq] = e
                last = e
                uniq += 1

        return uniq

