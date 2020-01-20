class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rottens = deque()
        t = 0
        
        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == 2:
                    rottens.append((i, j, t))
        
        def adjs(i, j):
            for a, b in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
                    yield a, b
        
        while rottens:
            i, j, t = rottens.popleft()
            
            for a, b in adjs(i, j):
                if grid[a][b] == 1:
                    grid[a][b] = 2
                    rottens.append((a, b, t+1))
        
        if any(1 in row for row in grid):
            return -1
                
        return t