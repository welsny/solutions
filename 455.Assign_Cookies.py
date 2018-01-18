#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        g_index, s_index = 0, 0
        result = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                result += 1
                s_index += 1
                g_index += 1
            else:
                s_index += 1

        return result
