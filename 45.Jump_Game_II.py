class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        First solution: O(N^2) time, O(N) space
        """
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0

        for i, n in enumerate(nums):
            for j in range(1, n+1):
                if i+j < len(nums):
                    jumps[i+j] = min(jumps[i+j], 1 + jumps[i])

        return jumps[-1]

    def jump(self, nums: List[int]) -> int:
        """
        Second solution: O(N) time, O(1) space
        """
        jumps = 0
        c_max = 0
        n_max = 0

        for i, n in enumerate(nums):
            n_max = max(n_max, i+n)

            if i == len(nums)-1:
                return jumps

            if i == c_max:
                jumps += 1
                c_max = n_max
