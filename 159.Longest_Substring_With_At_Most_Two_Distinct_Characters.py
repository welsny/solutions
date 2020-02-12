#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct_from_20161230(self, s):
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

    def lengthOfLongestSubstringTwoDistinct(self, s):
        res = i = 0
        d = {}

        for j, char in enumerate(s):
            d[char] = j
            if len(d) > 2:
                k, last_seen = min(d.items(), key=lambda item: item[1])
                del d[k]
                i = last_seen + 1
            res = max(res, j-i+1)

        return res
