#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        pts = []

        for op in ops:
            if op == "+":
                pts.append(pts[-1] + pts[-2])
            elif op == "D":
                pts.append(2*pts[-1])
            elif op == "C":
                pts.pop()
            else:
                pts.append(int(op))

        return sum(pts)

