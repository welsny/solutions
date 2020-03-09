from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = defaultdict(list)
        for p, c in zip(ppid, pid):
            tree[p].append(c)

        res = []
        stack = [kill]
        while stack:
            k = stack.pop()
            res.append(k)
            stack.extend(tree[k])
        return res
