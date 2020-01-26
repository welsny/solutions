class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not k or not nums:
            return 0

        i = ct = 0
        curr = 1

        for j, num in enumerate(nums):
            curr *= num
            while i <= j and curr >= k:
                curr //= nums[i]
                i += 1
            ct += j - i + 1

        return ct
