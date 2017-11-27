#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        sums = [(n1, n2) for n1 in nums1 for n2 in nums2]
        return sorted(sums, key=sum)[:k]

