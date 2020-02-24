from collections import deque

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        Implementation using BFS and `set`, which is cleaner syntax-wise in my opinion:
        """
        def adjs(i, j):
            for x, y, in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(A) and 0 <= y < len(A[0]):
                    yield x, y

        curr = deque()
        seen = set()

        for i, row in enumerate(A):
            for j, space in enumerate(row):
                if space:
                    break
            if space:
                curr.append((i, j))
                seen.add((i, j))
                break

        while curr:
            i, j = curr.popleft()

            for x, y in adjs(i, j):
                if A[x][y] and (x, y) not in seen:
                    curr.append((x, y))
                    seen.add((x, y))

        curr = deque((0, i, j) for i, j in seen)
        while curr:
            d, i, j = curr.popleft()

            for x, y in adjs(i, j):
                if (x, y) not in seen:
                    if A[x][y]:
                        return d
                    seen.add((x, y))
                    curr.append((d+1, x, y))

    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        Solution using a 2D array for `seen`, which uses less memory:
        """
        def adjs(i, j):
            for x, y, in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(A) and 0 <= y < len(A[0]):
                    yield x, y

        curr = deque()
        seen = [[False for _ in row] for row in A]

        for i, row in enumerate(A):
            for j, space in enumerate(row):
                if space:
                    break
            if space:
                curr.append((i, j))
                seen[i][j] = True
                break

        while curr:
            i, j = curr.popleft()

            for x, y in adjs(i, j):
                if A[x][y] and not seen[x][y]:
                    curr.append((x, y))
                    seen[x][y] = True

        curr = deque((0, i, j) for i, row in enumerate(seen) for j, s in enumerate(row) if s)
        while curr:
            d, i, j = curr.popleft()

            for x, y in adjs(i, j):
                if not seen[x][y]:
                    if A[x][y]:
                        return d
                    seen[x][y] = True
                    curr.append((d+1, x, y))
