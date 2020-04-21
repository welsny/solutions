#!/usr/bin/env python3

from collections import defaultdict

class StreamChecker:

    def __init__(self, words: List[str]):
        TrieNode = lambda: defaultdict(TrieNode)
        self.trie = TrieNode()
        for w in words:
            reduce(dict.__getitem__, reversed(w), self.trie)['#'] = True
        self.stream = ''
        self.max = max(len(w) for w in words)

    def query(self, letter: str) -> bool:
        self.stream = (letter + self.stream)[:self.max]

        curr = self.trie
        for char in self.stream:
            if char in curr:
                curr = curr[char]
                if '#' in curr:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
