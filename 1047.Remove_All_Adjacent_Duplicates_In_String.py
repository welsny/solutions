class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
