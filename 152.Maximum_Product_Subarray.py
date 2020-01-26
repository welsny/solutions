class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        c_min = c_max = res = nums[0]

        for n in nums[1:]:
            cands = [n, n*c_min, n*c_max]
            c_min, c_max = min(cands), max(cands)
            res = max(res, c_max)

        return res
