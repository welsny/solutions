#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

class Solution:
    """
    Original solution from March 2018:

    O(N) time
    O(N) space
    """
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)

        result = 0
        targets = defaultdict(int)
        for n in sums:
            result += targets[n]
            targets[k+n] += 1
        return result

from collections import defaultdict

class Solution:
    """
    We don't need to store an array of the sums since we only use
    the most recent one. We still use `seen` so it is still linear space.

    O(N) time
    O(N) space
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        s = res = 0
        for n in nums:
            s += n
            res += seen[s-k]
            seen[s] += 1
        return res
