class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        First approach that removes edges once we've traversed them:
        """
        res = []

        def dfs(path, g):
            curr = path[-1]
            if curr == len(graph)-1:
                res.append(path)

            adjs = g[curr]
            for i, adj in enumerate(adjs):
                g[curr] = adjs[:i] + adjs[i+1:]
                dfs(path + [adj], g)
                g[curr] = adjs

        dfs([0], graph)
        return res

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        Since they tell us that the graph is acyclical, we don't need to remove vertices:
        """
        res = []

        def dfs(path):
            curr = path[-1]
            if curr == len(graph)-1:
                res.append(path)
            for adj in graph[curr]:
                dfs(path + [adj])

        dfs([0])
        return res
