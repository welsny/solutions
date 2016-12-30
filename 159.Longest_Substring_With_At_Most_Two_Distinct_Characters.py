#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}

        result = 0
        start, end = 0, 0

        while end < len(s):
            if len(counts) < 2:
                if s[end] in counts:
                    counts[s[end]] += 1
                else:
                    counts[s[end]] = 1

            elif s[end] in counts:
                counts[s[end]] += 1

            else:
                # increment 'start' until the string is valid again
                counts[s[end]] = 1
                while len(counts) > 2:
                    counts[s[start]] -= 1
                    if counts[s[start]] == 0:
                        del counts[s[start]]
                    start += 1

            # Loop invariant: substring is valid at this point of the loop. 
            if end - start + 1 > result:
                result = end - start + 1

            end += 1

        return result

