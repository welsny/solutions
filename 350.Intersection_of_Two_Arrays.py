#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        cts1, cts2 = Counter(nums1), Counter(nums2)

        result = []
        for num, ct in cts1.items():
            if num in cts2:
                result += [num] * min(ct, cts2[num])

        return result

