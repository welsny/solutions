class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        res = 0
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                matrix[i][j] = int(n)
                if i:
                    matrix[i][j] += matrix[i-1][j]
                if j:
                    matrix[i][j] += matrix[i][j-1]
                if i and j:
                    matrix[i][j] -= matrix[i-1][j-1]

                for k in range(res, min(i, j)+2):
                    c = matrix[i][j]
                    if i - k >= 0:
                        c -= matrix[i-k][j]
                    if j - k >= 0:
                        c -= matrix[i][j-k]
                    if i - k >= 0 and j - k >= 0:
                        c += matrix[i-k][j-k]

                    if c == k**2:
                        res = max(res, k)

        return res**2
