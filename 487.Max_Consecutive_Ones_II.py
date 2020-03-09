class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        """
        DP using chunking:

        O(N) time
        O(N) space
        """
        ct = 0

        chunks = {} # start_index: length
        for i, n in enumerate(nums):
            if n:
                ct += 1
            else:
                chunks[i-ct] = ct
                ct = 0

        return max(l + int(i+l < len(nums)) + chunks.get(i+l+1, 0) for i, l in chunks.items())

    def findMaxConsecutiveOnes(self, nums):
        """
        Two-pointer:

        O(N) time
        O(1) space
        """
        res = l = ct = 0
        for r, num in enumerate(nums):
            if not num:
                ct += 1

            while ct > 1:
                if not nums[l]:
                    ct -= 1
                l += 1

            res = max(res, r-l+1)

        return res
