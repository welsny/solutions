from collections import defaultdict
from heapq import nsmallest

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        trie_node = lambda: defaultdict(trie_node)
        self.root = trie_node()

        for s, t in zip(sentences, times):
            self.insert(s, t)

        self.curr = self.root
        self.curr_query = ''

    def insert(self, s, t):
        curr = self.root
        for char in s:
            curr = curr[char]
            curr['#'][s] = t

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.curr_query, self.curr['#'].get(self.curr_query, 0)+1)
            self.curr = self.root
            self.curr_query = ''
            return []

        else:
            self.curr = self.curr[c]
            self.curr_query += c
            return nsmallest(3, self.curr['#'], key=(lambda x: (-self.curr['#'].get(x, 0), x)))


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
