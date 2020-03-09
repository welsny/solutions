class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1, '']]
        ct = 0
        for char in s:
            if char.isnumeric():
                ct *= 10
                ct += int(char)
                continue
            
            if char == '[':
                stack.append([ct, ''])
            elif char == ']':
                mult, ss = stack.pop()
                stack[-1][-1] += mult*ss
            else:
                stack[-1][-1] += char
            ct = 0

        return stack[-1][-1]