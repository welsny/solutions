from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain = defaultdict(int)

        for w in sorted(words, key=len):
            for i, _ in enumerate(w):
                chain[w] = max(chain[w], 1+chain[w[:i] + w[i+1:]])

        return max(chain.values())