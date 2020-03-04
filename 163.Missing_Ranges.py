class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []

        nums = [lower-1] + nums + [upper+1]
        for n, m in zip(nums, nums[1:]):
            if m-n == 2:
                res.append(f'{n+1}')
            elif m-n > 2:
                res.append(f'{n+1}->{m-1}')

        return res
