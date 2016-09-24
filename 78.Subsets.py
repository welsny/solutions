#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def subset(seq, acc=[]):
            if not seq:
                result.append(acc)
            else:
                subset(seq[1:], acc + [seq[0]])
                subset(seq[1:], acc)
        subset(nums)

        return result

