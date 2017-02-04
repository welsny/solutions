#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = set(range(n))

        while len(s) > 1:
            a, b = s.pop(), s.pop()
            if knows(a, b):
                s.add(b)
            else:
                s.add(a)

        c = s.pop()

        return c if all(knows(i, c) and not knows(c,i) for i in range(n) if i != c) else -1

