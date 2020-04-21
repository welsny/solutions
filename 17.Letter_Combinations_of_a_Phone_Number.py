#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        comb = {2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z']}

        curr = ['']
        for d in digits:
            next = []
            for i in comb[int(d)]:
                for j in curr:
                    next.append(j+i)
            curr = next

        return curr

