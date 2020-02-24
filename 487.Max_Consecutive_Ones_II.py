class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        ct = 0

        chunks = {} # start_index: length
        for i, n in enumerate(nums):
            if n:
                ct += 1
            else:
                chunks[i-ct] = ct
                ct = 0

        return max(l + int(i+l < len(nums)) + chunks.get(i+l+1, 0) for i, l in chunks.items())
