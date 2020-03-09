class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not k:
            return any(not i and not j for i, j in zip(nums,nums[1:]))

        s = 0
        targs = {0: -1}

        for i, n in enumerate(nums):
            s += n
            s %= abs(k)
            if s in targs and i-targs[s] >= 2:
                return True
            if s not in targs:
                targs[s] = i

        return False
