from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        neighs = defaultdict(list)
        for w in wordList:
            for i, _ in enumerate(w):
                neighs[w[:i] + '*' + w[i+1:]].append(w)

        dq = deque([(beginWord, 1)])
        while dq:
            w, d = dq.popleft()

            if w == endWord:
                return d

            for i, _ in enumerate(w):
                k = w[:i] + '*' + w[i+1:]
                for neigh in neighs[k]:
                    if neigh in wordList:
                        dq.append((neigh, d+1))
                        wordList.remove(neigh)

        return 0