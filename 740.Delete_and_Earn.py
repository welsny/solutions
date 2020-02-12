class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] + [0] * max(nums, default=0)

        for n in nums:
            dp[n] += n

        for i, points in enumerate(dp):
            if i < 2:
                continue
            dp[i] = max(dp[i-1], points+dp[i-2])

        return dp[-1]
