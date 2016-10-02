#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

# TODO: Improve effeciency by keeping a list of primes and using DP to check primality

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0

        for i in range(2, n):
            if self.is_prime(i):
                result += 1

        return result

    def is_prime(self, n):

        for i in range(2, 2 + int(ceil(sqrt(n)))):
            if n % i == 0:
                return False

        return True

