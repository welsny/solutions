from collections import defaultdict

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = defaultdict(list)
        dp[0, 0] = ['']
        
        for i in range(n+1):
            for j in range(i+1):
                if i:
                    dp[i, j].extend([s+'(' for s in dp[i-1, j]])
                if j:
                    dp[i, j].extend([s+')' for s in dp[i, j-1]])
        
        return dp[n, n]