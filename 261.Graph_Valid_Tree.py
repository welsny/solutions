from collections import defaultdict, deque

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        adjs = defaultdict(set)
        for i, j in edges:
            adjs[i].add(j)
            adjs[j].add(i)

        dq = deque([0])
        seen = set()
        while dq:
            node = dq.popleft()
            if node in seen:
                return False
            seen.add(node)
            for adj in adjs[node]:
                adjs[adj].remove(node)
                dq.append(adj)

        return len(seen) == n
