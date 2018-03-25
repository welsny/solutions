#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ct = Counter(s)
        for i, char in enumerate(s):
            if ct[char] == 1:
                return i
        return -1

