#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        items = []

        for i in path.split('/'):
            if i in ['', '.']:
                continue
            elif i == '..':
                if items:
                    items.pop()
            else:
                items.append(i)

        return '/'+'/'.join(items)

