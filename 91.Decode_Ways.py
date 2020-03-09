class Solution:
    def numDecodings(self, s: str) -> int:
        curr = prev = 1
        for i, n in enumerate(s):
            n = int(n)

            if i and s[i-1] in ["1", "2"]:
                n2 = 10*int(s[i-1]) + n
                if n2 > 26:
                    prev = curr
                elif not n:
                    curr, prev = prev, curr
                else:
                    curr, prev = curr+prev, curr
            elif not n:
                return 0
            else:
                prev = curr

        return curr
