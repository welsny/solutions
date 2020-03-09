from collections import defaultdict

class Trie:

    def __init__(self, end=False):
        """
        Initialize your data structure here.
        """
        self.end = end
        self.d = defaultdict(Trie)

    def insert(self, w: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not w:
            self.end = True
        else:
            self.d[w[0]].insert((len(w) > 1 and w[1:]) or '')

    def search(self, w: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not w:
            return self.end
        return w[0] in self.d and self.d[w[0]].search((len(w) > 1 and w[1:]) or '')

    def startsWith(self, p: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return not p or p[0] in self.d and self.d[p[0]].startsWith((len(p) > 1 and p[1:]) or '')
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)