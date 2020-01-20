#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ca = a.split('+')
        rb, cb = b.split('+')
        ca, cb = ca[:-1], cb[:-1]
        ra, rb, ca, cb = (int(i) for i in (ra, rb, ca, cb))
        return '{}+{}i'.format(ra*rb - ca*cb, ra*cb + rb * ca)

