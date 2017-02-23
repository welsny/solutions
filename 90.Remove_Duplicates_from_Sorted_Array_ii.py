#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last = None
        index = 0
        allow_dupe = False

        for e in nums:
            if last is None or e != last or allow_dupe:
                nums[index] = e
                allow_dupe = (e != last)
                last = e
                index += 1

        return index

