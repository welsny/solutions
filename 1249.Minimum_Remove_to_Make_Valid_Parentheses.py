class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_pop = []
        opens = []
        for i, char in enumerate(s):
            if char == '(':
                opens.append(i)
            if char == ')':
                if opens:
                    opens.pop()
                else:
                    to_pop.append(i)

        to_pop = set(to_pop) | set(opens)
        return ''.join(c for i, c in enumerate(s) if i not in to_pop)
