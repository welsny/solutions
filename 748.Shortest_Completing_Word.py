class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        lp = [char for char in licensePlate.lower() if not char.isnumeric() and not char == ' ']
        lp_ct = Counter(lp)
        res = None
        for w in words:
            w_ct = Counter(w)
            if not lp_ct - w_ct:
                if not res:
                    res = w
                else:
                    res = min(res, w, key=len)
        return res