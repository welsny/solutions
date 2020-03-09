from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(defaultdict)
        for start, dest, price in flights:
            graph[start][dest] = price

        cheapest = defaultdict(lambda: float('inf'))
        cheapest[src] = 0

        curr = [src]
        for i in range(K+1):
            next, cp = set(), cheapest.copy()
            for c in curr:
                for dest, price in graph[c].items():
                    if cheapest[c] + price < cp[dest]:
                        cp[dest] = cheapest[c] + price
                        next.add(dest)
            curr, cheapest = next, cp

        return cheapest.get(dst, -1)
