#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ct = Counter(p)
        curr = Counter(s[:len(p)])
        result = [0] if ct == curr else []

        for i in range(1, len(s)-len(p)+1):
            curr[s[i-1]] -= 1
            if not curr[s[i-1]]:
                del curr[s[i-1]]
            curr[s[i-1+len(p)]] += 1

            if curr == ct:
                result.append(i)

        return result

