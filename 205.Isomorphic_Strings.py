#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ct_s = OrderedDict()
        ct_t = OrderedDict()

        for i, c in enumerate(s):
            if c not in ct_s:
                ct_s[c] = [i]
            else:
                ct_s[c].append(i)

        for i, c in enumerate(t):
            if c not in ct_t:
                ct_t[c] = [i]
            else:
                ct_t[c].append(i)

        return list(ct_s.values()) == list(ct_t.values())

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for c, c2 in zip(s, t):
            if c not in d:
                d[c] = c2
            elif d[c] != c2:
                return False

        return len(d.values()) == len(set(d.values()))
