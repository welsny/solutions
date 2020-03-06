class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for i, c in enumerate(order)}

        def is_less_than(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return order[c1] < order[c2]
            return len(w1) < len(w2)

        return all(is_less_than(w1, w2) for w1, w2 in zip(words, words[1:]))
