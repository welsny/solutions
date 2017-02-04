#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = set([''])

        while result:
            next = set()
            for w in wordDict:
                 for r in result:
                    if r+w == s:
                        return True
                    if len(r+w) < len(s) and r+w == s[:len(r+w)]:
                        next.add(r+w)
            result = next

        return False
