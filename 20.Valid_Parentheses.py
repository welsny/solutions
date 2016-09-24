#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        reqs = []

        for char in s:
            if char == '(':
                reqs.append(')')
            elif char == '{':
                reqs.append('}')
            elif char == '[':
                reqs.append(']')

            else:
                if not reqs or char != reqs.pop():
                    return False

        return not reqs

