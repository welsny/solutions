#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Binary Search

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        while result*result < int(x):
            result += 1

        return result

