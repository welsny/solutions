from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prereq, c in prerequisites:
            graph[prereq].append(c)

        for n in range(numCourses):
            curr = [(n, set([n]))]
            while curr:
                c, seen = curr.pop()

                for adj in graph[c]:
                    if adj in seen:
                        return False
                    curr.append((adj, seen | set([adj])))

            del graph[n]

        return True
