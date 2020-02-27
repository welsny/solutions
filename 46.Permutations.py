class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def comb(curr, remaining):
            if not remaining:
                res.append(curr)
            for i, n in enumerate(remaining):
                comb(curr + [n], remaining[:i] + remaining[i+1:])

        comb([], nums)
        return res