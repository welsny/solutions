#!/usr/bin/env python
# -*- coding: utf-8 -*-

ass Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counts = {}

        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1

        for char in t:
            if char not in counts:
                return False
            else:
                counts[char] -= 1

        return all(value == 0 for key, value in counts.items())

