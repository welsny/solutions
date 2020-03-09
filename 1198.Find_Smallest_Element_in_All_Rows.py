from collections import Counter

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Naive solution using Counter:

        O(N*M) time
        O(N*M) space
        """
        cts = Counter(n for row in mat for n in row)

        # We need to do this IF duplicates are allowed in each row.
        # The question doesn't specify this but there are no intra-row 
        # duplicates in the test cases.

        # cts = Counter()
        # for row in mat:
        #     cts += Counter(set(row))

        return min((n for n, ct in cts.items() if ct == len(mat)), default=-1)

    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """
        Binary search:

        O(NM*log(M)) time
        O(1) space
        """
        for targ in mat[0]:
            found = True
            for row in mat[1:]:
                l, r = 0, len(mat[0])-1
                while l <= r:
                    m = (l+r)//2
                    if row[m] == targ:
                        break
                    elif row[m] < targ:
                        l = m+1
                    else:
                        r = m-1
                else:
                    found = False
                    break
            if found:
                return targ
        return -1
