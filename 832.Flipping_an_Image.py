#!/usr/bin/env python3

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(A):
            A[i] = row[::-1]
            for j, pixel in enumerate(A[i]):
                A[i][j] = 1 - pixel
        return A
