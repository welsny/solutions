from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        graph = defaultdict(set)

        for w, w2 in pairs:
            graph[w].add(w2)
            graph[w2].add(w)

        for w, w2 in zip(words1, words2):
            if w != w2 and w2 not in graph[w]:
                return False

        return True
