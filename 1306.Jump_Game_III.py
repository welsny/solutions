class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        curr = {start}
        seen = {start}

        while curr:
            next = set()
            for c in curr:
                if not arr[c]:
                    return True
                for n in (c-arr[c], c+arr[c]):
                    if 0 <= n < len(arr) and n not in seen:
                        next.add(n)
            seen |= next
            curr = next

        return False