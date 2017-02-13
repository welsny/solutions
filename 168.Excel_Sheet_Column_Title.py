#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''

        # 65 -> A
        while n:
            n -= 1
            result = chr(65 + n%26) + result
            n /= 26

        return result
