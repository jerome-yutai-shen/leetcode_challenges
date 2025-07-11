# -*- coding: utf-8 -*-
"""
Created on Jan 14 22:46:28 2024

@author: Jerome Yutai Shen

711
"""

from typing import List


class Solution1:

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


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(r, c, direction, path):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                path.append(direction)
                dfs(r + 1, c, 'D', path)
                dfs(r - 1, c, 'U', path)
                dfs(r, c + 1, 'R', path)
                dfs(r, c - 1, 'L', path)
                path.append('B')
            return path

        rows, cols = len(grid), len(grid[0])
        shapes = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = tuple(dfs(r, c, 'O', []))  # 'O' 是起点标记
                    # print(shape)
                    shapes.add(shape)

        return len(shapes)
