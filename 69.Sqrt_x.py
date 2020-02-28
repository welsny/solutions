class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            m = (l+r)//2
            if m**2 == x:
                return m
            elif m**2 < x:
                l, r = m+1, r
            else:
                l, r = l, m-1

        return r
