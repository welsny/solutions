#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
from collections import Counter, defaultdict


class Solution(object):
    """
    First solution from 2018-07-25:
    """
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cts = Counter(words)

        reverse_cts = defaultdict(list) # Key: Ct -- Value: [Words with given Ct]
        for word, ct in cts.items():
            reverse_cts[ct].append(word)

        result = []
        for ct in heapq.nlargest(k, reverse_cts):
            result += heapq.nsmallest(k - len(result), reverse_cts[ct])
        return result

# # # # #

from collections import Counter
from heapq import nsmallest


class Solution:
    """
    Second solution which is better, but is slightly slower:
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ct = Counter(words)
        return nsmallest(k, ct, key=lambda x: (-ct[x], x))
