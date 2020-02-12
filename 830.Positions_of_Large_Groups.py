class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i = 0
        result = []

        for j, char in enumerate(S):
            if j == len(S) - 1 or S[j+1] != S[i]:
                if j - i >= 2:
                    result.append([i, j])
                i = j + 1

        return result
