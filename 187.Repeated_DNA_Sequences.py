#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()

        curr = deque(s[:10])
        seen = set([''.join(curr)])

        for c in s[10:]:
            curr.popleft()
            curr.append(c)

            seq = ''.join(curr)
            if seq in seen:
                result.add(seq)
            else:
                seen.add(seq)

        return list(result)

