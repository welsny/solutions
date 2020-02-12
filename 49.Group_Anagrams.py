#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)

        for s in strs:
            d[''.join(sorted(s))].append(s)

        return list(d.values())
