#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0 for t in temperatures]
        next_occurance = [float('-Inf')] * 102

        for i, temp in enumerate(temperatures[::-1]):
            result[-i-1] = i - max(next_occurance[temp+1:])
            next_occurance[temp] = i

        return [0 if i == float('Inf') else i for i in result]

