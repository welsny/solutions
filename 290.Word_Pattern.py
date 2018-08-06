#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}

        if len(pattern) != len(str.split()): return False

        for char, word in zip(pattern, str.split()):
            if char not in d:
                d[char] = word
            elif d[char] != word:
                return False

        seen = set()
        for v in d.values():
            if v in seen:
                return False
            seen.add(v)

        return True

