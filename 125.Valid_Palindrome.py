#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(char for char in s.lower() if char.isalnum())
        return all(i==j for i, j in zip(s, s[::-1]))

