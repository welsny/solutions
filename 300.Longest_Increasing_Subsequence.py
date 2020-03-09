class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = []

        for i, n in enumerate(nums):
            length = 1
            for j in range(i+1):
                if n > nums[j]:
                    length = max(length, longest[j]+1)
            longest.append(length)

        return max(longest, default=0)
