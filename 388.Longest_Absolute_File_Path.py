class Solution:
    """
    First successful attempt using a stack-like solution:
    """
    def lengthLongestPath(self, input: str) -> int:
        stack = []

        longest = 0
        indent = -1
        for line in input.split('\n'):
            nest = line.count('\t')
            line = line[nest:]
            if nest > indent:
                stack.append(line)
                indent += 1
            else:
                for i in range(indent-nest+1):
                    stack.pop()
                indent = nest
                stack.append(line)

            if '.' in stack[-1]:
                longest = max(longest, len('/'.join(stack)))

        return longest

class Solution:
    """
    Final solution after cleaning up code from above:
    """
    def lengthLongestPath(self, input: str) -> int:
        stack = []

        longest = 0
        for line in input.split('\n'):
            nest = line.count('\t')
            line = line[nest:]
            stack = stack[:nest]

            stack.append(line)

            if '.' in stack[-1]:
                longest = max(longest, len('/'.join(stack)))

        return longest
