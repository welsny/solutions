#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for str in strs:
            key = ''.join(sorted(str))

            if key not in anagrams:
                anagrams[key] = [str]
            else:
                anagrams[key].append(str)

        return [i for i in anagrams.values()]

