#!/usr/bin/env python
# -*- coding: utf-8 -*-

import heapq
from collections import Counter, defaultdict

class Solution(object):
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

