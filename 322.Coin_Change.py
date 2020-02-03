class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        
        for i in range(amount):
            m = float('inf')
            for c in coins:
                if len(dp) >= c and dp[-c] >= 0:
                    m = min(m, 1+dp[-c])
            dp.append(m)

        return dp[-1] if dp[-1] != float('inf') else -1