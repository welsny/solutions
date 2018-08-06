#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        loc = {c: i for i, c in enumerate(S)}

        result = []

        start = end = 0
        for i, c in enumerate(S):
            end = max(end, loc[c])
            if i == end:
                result.append(end - start + 1)
                start = end = end + 1

        return result

