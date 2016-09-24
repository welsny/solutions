#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for i, str in enumerate(grid):
            for j, char in enumerate(str):
                if char == '1':
                    self.r_rm_land(i, j, grid)
                    count += 1

        return count

    def r_rm_land(self, i, j, grid):
        try:
            if grid[i][j] == '1':
                grid[i][j] = '0'
                self.r_rm_land(i + 1, j, grid)
                if i > 0:
                    self.r_rm_land(i - 1, j, grid)
                self.r_rm_land(i, j + 1, grid)
                if j > 0:
                    self.r_rm_land(i, j - 1, grid)
        except IndexError:
            pass

