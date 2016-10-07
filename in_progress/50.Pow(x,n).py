#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Get prime factorization for N. At each recursive step, raise x
      # to the power of each prime that amount. 

class Solution(object):
    def myPow(self, x, n, acc=1):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return acc

        elif n < 0:
            return self.myPow(1/x, -n)

        else:
            return self.myPow(x, n-1, x*acc)

