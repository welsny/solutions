class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [0]

        for n in nums:
            sums.append(n + sums[-1])

        min_seen = 0
        res = float('-inf')

        for s in sums[1:]:
            res = max(res, s-min_seen)
            min_seen = min(min_seen, s)

        return res
