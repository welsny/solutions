#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict, Counter

class Solution:
    def fourSumCount(self, A, B, C, D):
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

