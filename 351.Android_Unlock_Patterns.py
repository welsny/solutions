class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.m, self.n = m, n

        self.selected = [[False for _ in range(3)] for _ in range(3)]
        self.res = 0

        for i in range(3):
            for j in range(3):
                self.dfs(i, j, 0)

        return self.res

    def adjs(self, x, y):
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1],
                       [0, -1], [0, 1],
                       [1, -1], [1, 0], [1, 1],
                       [-2, -1], [-2, 1],
                       [-1, -2], [-1, 2],
                       [1, -2], [1, 2],
                       [2, -1], [2, 1]]:
            i, j = x+dx, y+dy
            if not (0 <= i < 3 and 0 <= j < 3):
                continue
            if not self.selected[i][j]:
                yield i, j
            else:
                i, j = i+dx, j+dy
                if (0 <= i < 3 and 0 <= j < 3) and not self.selected[i][j]:
                    yield i, j

    def dfs(self, x, y, ct):
        self.selected[x][y] = True
        ct += 1
        if self.m <= ct <= self.n:
            self.res += 1
        if ct < self.n:
            for i, j in self.adjs(x, y):
                self.dfs(i, j, ct)
        self.selected[x][y] = False
