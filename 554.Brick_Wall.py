#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        ct = defaultdict(int)
        for row in wall:
            for i, length in enumerate(row):
                if not i:
                    continue
                ct[row[i-1]] += 1
                row[i] += row[i-1]

        return len(wall) - max(ct.values()) if ct else len(wall)

