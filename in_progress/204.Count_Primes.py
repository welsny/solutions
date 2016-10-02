#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

# TODO: Improve effeciency?

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []

        for i in range(2, n):
            if any(i%p==0 for p in primes):
                continue
            else:
                primes.append(i)

        return len(primes)

