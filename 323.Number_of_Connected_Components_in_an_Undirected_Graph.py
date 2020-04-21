#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)

        ct = 0
        traversed = set()
        for i in range(n):
            if i in traversed:
                continue

            ct += 1

            seen = set([i])
            stack = [i]
            while stack:
                i = stack.pop()

                for adj in graph[i]:
                    if adj not in seen:
                        stack.append(adj)
                        traversed.add(adj)
                        seen.add(adj)
        return ct
