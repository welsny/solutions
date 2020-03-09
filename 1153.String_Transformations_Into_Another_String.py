class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        convs = {}

        for c1, c2 in zip(str1, str2):
            if c1 in convs and convs[c1] != c2:
                return False
            convs[c1] = c2

        return str1 == str2 or len(set(str2)) != 26
