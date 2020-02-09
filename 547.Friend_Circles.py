from collections import deque

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        traversed = set()
        res = 0
        for i in range(len(M)):
            if i in traversed:
                continue

            seen = set([i])
            dq = deque([i])
            while dq:
                row = dq.popleft()
                for j, adj in enumerate(M[row]):
                    if adj and j not in seen:
                        seen.add(j)
                        dq.append(j)

            res += 1
            traversed.update(seen)

        return res
