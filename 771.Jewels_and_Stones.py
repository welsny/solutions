#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J = set(J)
        return sum(1 for s in S if s in J)

