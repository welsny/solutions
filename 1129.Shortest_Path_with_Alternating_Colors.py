#!/usr/bin/env python3

from collections import deque, defaultdict


class Solution:
    """
    First pass solution using BFS. We do each BFS pair separately:
    """
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        for s, e in red_edges:
            red[s].append(e)

        blue = defaultdict(list)
        for s, e in blue_edges:
            blue[s].append(e)

        def shortest_bfs(target):
            dq = deque([(0, 0, True), (0, 0, False)])

            seen = set()
            seen.add((0, True))
            seen.add((0, False))
            while dq:
                node, d, is_red = dq.popleft()

                if node == target:
                    return d

                if is_red:
                    adjs = blue[node]
                else:
                    adjs = red[node]

                for adj in adjs:
                    if (adj, is_red) not in seen:
                        dq.append((adj, d+1, not is_red))
                        seen.add((adj, is_red))

            return -1

        return [shortest_bfs(i) for i in range(n)]

    from collections import deque, defaultdict

class Solution:
    """
    It is unnecessary to do each traversal separately -- can just do it in a single pass:
    """
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        for s, e in red_edges:
            red[s].append(e)

        blue = defaultdict(list)
        for s, e in blue_edges:
            blue[s].append(e)

        def bfs():
            dq = deque([(0, 0, True), (0, 0, False)])

            seen = set()
            seen.add((0, True))
            seen.add((0, False))
            while dq:
                node, d, is_red = dq.popleft()

                res[node] = min(d, res[node])

                if is_red:
                    adjs = blue[node]
                else:
                    adjs = red[node]

                for adj in adjs:
                    if (adj, is_red) not in seen:
                        dq.append((adj, d+1, not is_red))
                        seen.add((adj, is_red))

        res = n*[float('inf')]
        bfs()
        return [r if r != float('inf') else -1 for r in res]
