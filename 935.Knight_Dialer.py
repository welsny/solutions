class Solution:
    def knightDialer(self, steps: int) -> int:
        adjs = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        cts = [1] * 10

        for _ in range(steps-1):
            next_cts = [0] * 10
            for i, ct in enumerate(cts):
                for a in adjs[i]:
                    next_cts[a] += ct
            cts = next_cts

        return sum(cts) % (10**9 + 7)
