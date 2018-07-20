#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    """
    First solution using numeric indicies and HashSet to check for duplicates.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        chars = set()

        result = 0

        while end < len(s):
            c = s[end]
            if c in chars:
                while s[start] != c and start != end:
                    chars.remove(s[start])
                    start += 1
                if start < end:
                    start += 1
            else:
                chars.add(c)

            end += 1
            result = max(result, end-start)

        return result

from collections import deque

class Solution:
    """
    Reimplementation using Deque.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dq = deque()
        result = 0

        for c in s:
            if c in dq:
                while len(dq):
                    if c == dq.popleft():
                        break
            dq.append(c)
            result = max(result, len(dq))

        return result

