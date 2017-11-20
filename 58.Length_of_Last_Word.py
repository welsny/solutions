#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if s.split() else 0

