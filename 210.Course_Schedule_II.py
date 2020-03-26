from collections import Counter, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        cts = Counter()
        for c, prereq in prerequisites:
            graph[prereq].append(c)
            cts[c] += 1

        res = []
        stack = [n for n in range(numCourses) if cts[n] == 0]
        while stack:
            n = stack.pop()

            res.append(n)
            for adj in graph[n]:
                cts[adj] -= 1
                if not cts[adj]:
                    stack.append(adj)
            del graph[n]

        return res if len(res) == numCourses else []
