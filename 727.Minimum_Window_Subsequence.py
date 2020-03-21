class Solution:
    """
    Initial approach -- 2D-DP. We only need the last two rows, so we do not need O(S*T) space:

    O(S*T) time
    O(S) space
    """
    def minWindow(self, S: str, T: str) -> str:
        if not S or not T:
            return ""

        dp = [float('inf') for _ in S]

        for i, t in enumerate(T):
            next_dp = []
            for j, _ in enumerate(dp):
                if S[j] == t:
                    if not i:
                        next_dp.append(1)
                    else:
                        next_dp.append(1+dp[j-1])
                else:
                    next_dp.append((not j and float('inf')) or 1+next_dp[j-1])
            dp = next_dp

        end, l = min(enumerate(dp), key=lambda x: (x[1], x[0]))
        return S[end-l+1:end+1] if l != float('inf') else ''
