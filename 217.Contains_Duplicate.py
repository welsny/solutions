#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False

