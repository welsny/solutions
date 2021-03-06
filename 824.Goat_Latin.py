#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for i, s in enumerate(S.split()):
            if s[0] in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
                result.append(s + 'ma' + 'a'*(i+1))
            else:
                result.append(s[1:] + s[0] + 'ma' + 'a'*(i+1))
        return ' '.join(result)

class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i, w in enumerate(S.split()):
            if w[0].lower() not in vowels:
                w = w[1:] + w[0]

            w += 'maa' + i*'a'
            res.append(w)

        return ' '.join(res)
