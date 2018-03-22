#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_count = Counter(moves)
        return move_count['U'] == move_count['D'] and move_count['L'] == move_count['R']
