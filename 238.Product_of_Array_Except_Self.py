class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[::1]

        for i in range(len(res)):
            if i:
                res[-i-1] *= res[-i]

        for i in range(len(nums)):
            if not i:
                res[0] = res[1]
            elif i == len(res)-1:
                res[-1] = nums[-2]
            else:
                nums[i] *= nums[i-1]
                res[i] = nums[i-1] * res[i+1]

        return res
