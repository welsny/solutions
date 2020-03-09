class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        res = []

        # Min:
        for i, n in enumerate(count):
            if n:
                res.append(i)
                break

        # Max:
        for i, n in enumerate(reversed(count)):
            if n:
                res.append(255-i)
                break

        # Mean:
        res.append(
            sum(i*ct for i, ct in enumerate(count))/sum(count)
        )

        # Median:
        sm = sum(count)
        s = sm//2 + sm % 2
        for i, ct in enumerate(count):
            s -= ct
            if not s and not sm % 2:
                j = i+1
                while not count[j]:
                    j += 1
                res.append((i+j)/2)
                break
            elif s <= 0:
                res.append(i)
                break

        # Mode:
        mode, _ = max(enumerate(count), key=lambda x: x[1])
        res.append(mode)

        return [float(r) for r in res]
