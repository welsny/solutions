class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        res = [""]

        for char in S:
            if char.isalpha():
                res = [s + char.lower() for s in res] + [s + char.upper() for s in res]
            else:
                res = [s + char for s in res]

        return res
