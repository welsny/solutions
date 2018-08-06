#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            if i > 0 and not len(s)%(i+1):
                n_splits, split_size = i+1, len(s)/(i+1)
                if all(len(set(s[j::split_size])) == 1 for j in range(split_size)):
                    return True
        return False

