# -*- coding: utf-8 -*-
"""
Created on Jun 22 00:10:44 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution(object):
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)

#######
class SolutionBFS:
    """
    @param grid: the 2D grid
    @return: the number of distinct islands
    """
    import collections

    def numDistinctIslands2(self, grid):
        n, m = len(grid), len(grid[0])
        visited = set()
        islands = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.BFS(grid, i, j, visited, islands)

        island_hash = { }
        for island in islands:
            represent = tuple(self.transform(island))
            island_hash[represent] = island_hash.get(represent, 0) + 1
        return len(island_hash)

    def BFS(self, grid, x, y, visited, islands):
        n, m = len(grid), len(grid[0])
        q = collections.deque([(x, y)])
        visited.add((x, y))
        index = 0
        while index < len(q):
            x, y = q[index]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newx, newy = x + dx, y + dy
                if (newx, newy) in visited or not (0 <= newx < n and 0 <= newy < m):
                    continue
                if grid[newx][newy] != 1:
                    continue
                q.append((newx, newy))
                visited.add((newx, newy))
            index += 1
        islands.append(q)

    def transform(self, island):
        island_trans = [[] for _ in range(8)]
        island_trans[0] = island
        island_move = [[] for _ in range(8)]
        for x, y in island:
            island_trans[1].append((x, -y))
            island_trans[2].append((-x, y))
            island_trans[3].append((-x, -y))
            island_trans[4].append((y, x))
            island_trans[5].append((y, -x))
            island_trans[6].append((-y, x))
            island_trans[7].append((-y, -x))
        for i, isl in enumerate(island_trans):
            min_x, min_y = float('inf'), float('inf')
            for x, y in isl:
                min_x, min_y = min(min_x, x), min(min_y, y)
            for x, y in isl:
                move_x, move_y = x - min_x, y - min_y
                island_move[i].append((move_x, move_y))
            island_move[i].sort()
        island_move.sort()
        return island_move[0]