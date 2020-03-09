from collections import defaultdict
from heapq import nsmallest

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        lookup = defaultdict(list)

        for w in products:
            for i, _ in enumerate(w):
                lookup[w[:i+1]].append(w)

        prefixes = [searchWord[:i+1] for i in range(len(searchWord))]
        return [nsmallest(3, lookup[p]) for p in prefixes]

"""
Optimizations to make:

    1) Can not store lookups for products that do not match the searchWord prefixes
       so that we do not store products that we wouldn't use in this call.
    2) Can do a heap operation in the inner loop instead of storing all product candidates before
       sorting.
"""
