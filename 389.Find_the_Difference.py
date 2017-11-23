#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list((Counter(t) - Counter(s)).keys())[0]

