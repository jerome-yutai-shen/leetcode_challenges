# -*- coding: utf-8 -*-
"""
Created on Jul 17 19:35:07 2022

@author: Jerome Yutai Shen

"""
from collections import deque


DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class SolutionBFS:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0

        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]


class SolutionUnionFind:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def unionfind(self, root: int, pre: list):
        son = root
        while (root != pre[root]):
            root = pre[root]
        while (son != root):
            tmp = pre[son]
            pre[son] = root
            son = tmp
        # print(type(root))
        return root, pre

    def connect(self, A: int, B: int, pre: list, ans: int):
        rootA, pre = self.unionfind(A, pre)
        rootB, pre = self.unionfind(B, pre)
        if (rootA != rootB):
            pre[rootB] = rootA
            ans -= 1
        return pre, ans

    def num_islands(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        pre, ans = [], 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pre += [i * m + j]
                if grid[i][j]:
                    ans += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    if (i + 1 < n and grid[i + 1][j]):
                        pre, ans = self.connect(i * m + j + m, i * m + j, pre, ans)
                    if (j + 1 < m and grid[i][j + 1]):
                        pre, ans = self.connect(i * m + j + 1, i * m + j, pre, ans)
        print(f"pre {pre}")

        return ans


if __name__ == "__main__":
    grid = [[1, 1, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    solution = SolutionUnionFind()
    ans = solution.num_islands(grid)
    solution1 = SolutionBFS()
    ans1 = solution1.num_islands(grid)
    print(ans, ans1)

    grid = [[1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1]]
    solution = SolutionUnionFind()
    ans = solution.num_islands(grid)
    solution1 = SolutionBFS()
    ans1 = solution1.num_islands(grid)
    print(ans, ans1)