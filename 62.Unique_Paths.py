#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        import scipy.misc
        return int(scipy.misc.comb(m+n-2, n-1))

