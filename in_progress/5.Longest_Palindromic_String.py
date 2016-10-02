#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: implement this in O(n^2) - strategy: find Palindrome seeds and bloom outwards

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''

        for i, start in enumerate(s):
            for j, end in s[i:]:
                if self.is_palindrome(s[i:i+j]) and j > len(result):
                    result = s[i:i+j]

        return result

    def is_palindrome(self, s):
        return all(i == j for i, j in zip(s, s[::-1]))

