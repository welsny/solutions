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

class Solution:
    def findContentChildren(self, g, s):
        """
        Improved solution. I just made some easy optimizations to my previous code without re-examining the approach. Made a lot of easy mistakes the first time around -- this is a good example of the importance of sleep and revisiting your own code!

        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        g_index, s_index = 0, 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
            s_index += 1

        return g_index

