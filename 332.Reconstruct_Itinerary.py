from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for i, j in sorted(tickets):
            graph[i].append(j)

        def dfs(curr, res, graph):
            if not any(graph.values()):
                return res

            adjs = graph[curr]
            for i, adj in enumerate(adjs):
                graph[curr] = adjs[:i] + adjs[i+1:]
                if sol := dfs(adj, res + [adj], graph):
                    return sol
                graph[curr] = adjs

        return dfs('JFK', ['JFK'], graph)
