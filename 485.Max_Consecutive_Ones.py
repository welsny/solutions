class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = res = 0

        for n in nums:
            if n:
                ct += 1
                res = max(res, ct)
            else:
                ct = 0

        return res
