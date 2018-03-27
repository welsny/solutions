#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nexts = {}

        curr = set()
        for n in nums2:
            for i in list(curr):
                if n > i:
                    nexts[i] = n
                    curr.remove(i)
            curr.add(n)

        return [nexts.get(i, -1) for i in nums1]
