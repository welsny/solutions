class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1

        for i, row in enumerate(dp):
            for j, _ in enumerate(row):
                if obstacleGrid[i][j]:
                    continue
                if j:
                    dp[i][j] += dp[i][j-1]
                if i:
                    dp[i][j] += dp[i-1][j]

        return dp[-1][-1]
