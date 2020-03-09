class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []

        if k == 1:
            return nums

        return [max(nums[i:i+k]) for i, _ in enumerate(nums[:-k+1])]
