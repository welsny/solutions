from collections import deque
from copy import copy

class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def adjs(self, i, j):
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[0]):
                yield x, y


    def updateMatrix(self, matrix):
        """
        Level-order traversal using cool set comprehension syntax:
        """
        self.matrix = matrix

        curr = {(i, j) for i, row in enumerate(matrix) for j, n in enumerate(row) if not n}
        seen = copy(curr)

        depth = 0
        while curr:
            curr = {(x, y) for i, j in curr for x, y in self.adjs(i, j) if (x, y) not in seen}
            for x, y in curr:
                matrix[x][y] = depth + 1

            seen |= curr
            depth += 1

        return matrix

    def updateMatrix(self, matrix):
        """
        Normal BFS using queue for slightly better memory usage:
        """
        self.matrix = matrix

        curr = deque((0, i, j) for i, row in enumerate(matrix) for j, n in enumerate(row) if not n)
        seen = [[not bool(n) for n in row] for row in matrix]

        while curr:
            d, i, j = curr.popleft()

            for x, y in self.adjs(i, j):
                if not seen[x][y]:
                    matrix[x][y] = d+1
                    seen[x][y] = True
                    curr.append((d+1, x, y))

        return matrix
