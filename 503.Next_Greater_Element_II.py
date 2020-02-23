from heapq import heappush, heappop

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        heap = [(float('inf'), -1)]  #  val, index

        for i, n in enumerate(nums):
            while n > heap[0][0]:
                _, j = heappop(heap)
                res[j] = n
            heappush(heap, (n, i))

        for i, n in enumerate(nums):
            while n > heap[0][0]:
                _, j = heappop(heap)
                res[j] = n

        return res
