class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        from collections import deque, Counter

        seen = {id: 0}

        dq = deque([(0, id)])

        while dq:
            l, id = dq.pop()

            for f in friends[id]:
                if l < level and f not in seen:
                    dq.append((l+1, f))
                    seen[f] = l+1

        cts = Counter()

        for f, l in seen.items():
            if l == level:
                for w in watchedVideos[f]:
                    cts[w] += 1

        return [v for v, ct in sorted(cts.items(), key=lambda x: (x[1], x[0]))]

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        from collections import Counter

        seen = set([id])
        curr = [id]

        for _ in range(level):
            next = []
            for c in curr:
                for f in friends[c]:
                    if f not in seen:
                        seen.add(f)
                        next.append(f)
            curr = next

        cts = Counter()
        for c in curr:
            for w in watchedVideos[c]:
                cts[w] += 1

        return [w for w, ct in sorted(cts.items(), key=lambda x: (x[1], x[0]))]

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        from collections import Counter

        seen, curr = {id}, {id}

        for _ in range(level):
            curr = {f for c in curr for f in friends[c] if f not in seen}
            seen |= curr

        cts = Counter(w for c in curr for w in watchedVideos[c])

        return sorted(cts.keys(), key=lambda x: (cts[x], x))
