from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        def adjs(i, j):
            for a, b in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= a < n and 0 <= b < m:
                    yield a, b

        old_color = image[sr][sc]

        if old_color == newColor:
            return image

        dq = deque([(sr, sc)])
        while dq:
            i, j = dq.popleft()
            for a, b in adjs(i, j):
                if image[a][b] == old_color:
                    dq.append((a, b))
            image[i][j] = newColor

        return image
