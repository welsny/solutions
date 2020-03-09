from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def adj(i, j):
            for a, b in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
                if 0 <= a < n and 0 <= b < m:
                    yield a, b

        def sink(i, j):
            dq = deque([[i, j]])
            size = 0

            while dq:
                i, j = dq.popleft()

                if not grid[i][j]:
                    continue

                size += 1
                grid[i][j] = 0
                for a, b in adj(i, j):
                    dq.append([a, b])

            return size

        res = 0
        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                if land:
                    res = max(res, sink(i,j))

        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            dq = deque([(i, j)])
            grid[i][j] = 0
            area = 0

            while dq:
                i, j = dq.pop()
                area += 1

                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
                        dq.append((x, y))
                        grid[x][y] = 0

            return area

        res = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n:
                    res = max(res, bfs(i, j))

        return res
