class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        res = i = 0
        d = {}

        for j, char in enumerate(s):
            d[char] = j
            if len(d) > k:
                pop, last_seen = min(d.items(), key=lambda item: item[1])
                del d[pop]
                i = last_seen + 1
            res = max(res, j-i+1)

        return res
