class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, row in enumerate(triangle):
            if not i:
                continue

            for j, _ in enumerate(row):
                if j == 0:
                    row[j] += triangle[i-1][0]
                elif j == len(row)-1:
                    row[j] += triangle[i-1][-1]
                else:
                    row[j] += min(triangle[i-1][j-1], triangle[i-1][j])

        return min(triangle[-1])
