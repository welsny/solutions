class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        
        for i, n in enumerate(nums):
            if i > curr_max:
                return False
            curr_max = max(curr_max, i+n)
        
        return True
            