from collections import Counter, defaultdict
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        Prototype solution using dictionaries:

        O(N*M) time
        O(N+M) space
        """
        row_ct = defaultdict(list)
        col_ct = Counter()

        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == 'W':
                    continue

                col_ct[j] += 1
                # Limit the number of elements we store per row, which
                # decreases space complexity from N*M to N+M
                if len(row_ct[i]) <= 2:
                    row_ct[i].append(j)

        res = 0
        for i, js in row_ct.items():
            if len(js) != 1:
                continue
            if col_ct[js[0]] == 1:
                res += 1
        return res


    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        Using array instead of dictionaries (slightly faster):

        O(N*M) time
        O(N+M) space
        """
        n, m = len(picture), len(picture[0])

        row_ct = [[] for _ in range(n)]
        col_ct = [0 for _ in range(m)]
        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == 'W':
                    continue

                col_ct[j] += 1
                if len(row_ct[i]) <= 2:
                    row_ct[i].append(j)

        res = 0
        for i, js in enumerate(row_ct):
            if len(js) != 1:
                continue
            if col_ct[js[0]] == 1:
                res += 1
        return res
