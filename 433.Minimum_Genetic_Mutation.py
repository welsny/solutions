from collections import defaultdict, deque

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        neighs = defaultdict(list)

        for gene in bank:
            for i, _ in enumerate(gene):
                g = gene[:i] + '*' + gene[i+1:]
                neighs[g].append(gene)

        bank = set(bank)
        dq = deque([(start, 0)])
        while dq:
            gene, d = dq.popleft()

            if gene == end:
                return d

            for i, _ in enumerate(gene):
                g = gene[:i] + '*' + gene[i+1:]
                for neigh in neighs[g]:
                    if neigh in bank:
                        bank.remove(neigh)
                        dq.append((neigh, d+1))

        return -1
