from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        graph = defaultdict(set)

        for w, w2 in pairs:
            graph[w].add(w2)
            graph[w2].add(w)

        ct = 0
        word_map = {}
        for n in list(graph.keys()):
            if n not in graph:
                continue

            ct += 1
            seen = set([n])
            stack = [n]
            while stack:
                n = stack.pop()

                word_map[n] = ct
                for adj in graph[n]:
                    if adj not in seen:
                        seen.add(adj)
                        stack.append(adj)
                del graph[n]

        if len(words1) != len(words2):
            return False

        for w, w2 in zip(words1, words2):
            if w != w2 and (w not in word_map or w2 not in word_map or word_map[w] != word_map[w2]):
                return False
        return True
