class Solution:
    def expand(self, S: str) -> List[str]:
        res = ['']

        in_parens = False
        chars = []
        for char in S:
            if char == '{':
                in_parens = True
            elif char == '}':
                in_parens = False
                res = [r+c for r in res for c in sorted(chars)]
                chars = []
            elif in_parens:
                if char != ',':
                    chars.append(char)
            else:
                res = [r+char for r in res]

        return res
