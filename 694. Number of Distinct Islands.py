# -*- coding: utf-8 -*-
"""
Created on Jan 14 22:46:28 2024

@author: Jerome Yutai Shen

711
"""


class Solution:

    def __init__(self):
        self.n = 0
        self.m = 0
        self.dx = (0, 0, 1, -1)
        self.dy = (1, -1, 0, 0)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        islands = set()

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    aIsland = set()
                    self.dfs(i, j, grid, aIsland, i, j)
                    islands.add(tuple(aIsland))
        print(islands)
        return len(islands)

    def dfs(self, x, y, grid, aIsland, bx, by):
        grid[x][y] = 0
        aIsland.add((x - bx, y - by))
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if nx < 0 or nx >= self.n or ny < 0 or ny >= self.m or grid[nx][ny] != 1:
                continue
            self.dfs(nx, ny, grid, aIsland, bx, by)

