#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [n for n, ct in Counter(nums).most_common(k)]

