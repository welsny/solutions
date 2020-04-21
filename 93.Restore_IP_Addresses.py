class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        stack = [([], s)]
        while stack:
            curr, s = stack.pop()

            if len(curr) == 4:
                if not s:
                    res.append('.'.join(curr))
                continue

            for i in range(3):
                if i >= len(s):
                    break

                digits = s[:i+1]

                if digits == '0' or (digits[0] != '0' and int(digits) < 256):
                    stack.append((curr+[digits], s[i+1:]))

        return res
