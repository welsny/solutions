#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ct = Counter(s1)
        ct2 = Counter(s2[:len(s1)])

        for i, char in enumerate(s2[len(s1):]):
            if ct == ct & ct2:
                return True
            ct2[s2[i]] -= 1
            ct2[char] += 1

        return ct == ct & ct2

        # Less efficient one-liner:
        ct = Counter(s1)
        return any(Counter(s2[i:i+len(s1)]) == ct for i in range(len(s2)))
