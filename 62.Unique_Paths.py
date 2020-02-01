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


class Solution2:
    """
    Solution after revisiting the problem accidentally in 2020.

    Use `math.factorial` here which is faster than SciPy. Also I think
    the method names may have changed in SciPy since 2017.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial as f
        return int(f(m+n-2)/f(m-1)/f(n-1))
