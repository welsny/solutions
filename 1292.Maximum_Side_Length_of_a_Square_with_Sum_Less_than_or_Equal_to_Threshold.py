class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        res = 0

        for i, row in enumerate(mat):
            for j, _ in enumerate(row):
                if i:
                    mat[i][j] += mat[i-1][j]
                if j:
                    mat[i][j] += mat[i][j-1]
                if i and j:
                    mat[i][j] -= mat[i-1][j-1]

                sq_min, sq_max = max(1, res), min(i, j) + 2
                while sq_min < sq_max:
                    m = (sq_min + sq_max)//2

                    s = mat[i][j]
                    if m <= i:
                        s -= mat[i-m][j]
                    if m <= j:
                        s -= mat[i][j-m]
                    if m <= i and m <= j:
                        s += mat[i-m][j-m]

                    if s <= threshold:
                        res = max(res, m)
                        sq_min = m+1
                    else:
                        sq_max = m-1

        return res
