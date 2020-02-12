class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        res = 0

        for p in prices:
            min_price = min(min_price, p)
            res = max(res, p-min_price)

        return res
