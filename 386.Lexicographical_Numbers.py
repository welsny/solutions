#!/usr/bin/env python3

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n+1)), key=str)
