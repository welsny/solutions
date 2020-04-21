#!/usr/bin/env python3

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        def transform(w):
            w = w.lower()
            for v in vowels:
                w = w.replace(v, '*')
            return w

        d = set(wordlist)
        d_lower = {}
        d_vowel = {}
        for w in reversed(wordlist):
            d_lower[w.lower()] = w
            d_vowel[transform(w)] = w

        res = []
        for w in queries:
            lower = w.lower()
            vowel = transform(w)
            if w in d:
                res.append(w)
            elif lower in d_lower:
                res.append(d_lower[lower])
            elif vowel in d_vowel:
                res.append(d_vowel[vowel])
            else:
                res.append('')

        return res
