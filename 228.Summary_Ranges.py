class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = curr = nums[0]
        for n in nums[1:] + [float('inf')]:
            if n == curr+1:
                curr = n
                continue

            if start != curr:
                res.append(f'{start}->{curr}')
            else:
                res.append(f'{start}')

            start = curr = n

        return res
