class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        delts = [0] + [g*c for g, c in zip(grumpy, customers)]
        default = sum((1-g)*c for g, c in zip(grumpy, customers))

        max_delt = 0
        for i, d in enumerate(delts):
            if i < len(delts) - 1:
                delts[i+1] += d

        return default + max(d - delts[max(0, i-X)] for i, d in enumerate(delts))

