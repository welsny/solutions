#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cts = Counter(s)
        rev = defaultdict(list)

        for char, ct in cts.items():
            rev[ct].append(char)

        result = ""
        for ct, char_list in sorted(rev.items(), reverse=True):
            for char in char_list:
                result += ct*char
        return result

# # # # #

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cts = Counter(s)
        return ''.join([ct*c for c, ct in sorted(cts.items(), key=lambda x: -x[1])])
