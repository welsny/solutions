class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(nums):
            curr = prev = 0
            for n in nums:
                curr, prev = max(curr, n+prev), curr
            return curr

        return max(rob2(nums[1:]), rob2(nums[:-1]), len(nums) and nums[0])