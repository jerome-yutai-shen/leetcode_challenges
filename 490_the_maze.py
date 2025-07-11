# -*- coding: utf-8 -*-
"""
Created on Jun 24 23:17:24 2025

@author: Jerome Yutai Shen

"""
from typing import List
from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])
        # 此处切记用[[False for _ in range(n)] for _ in range(m)]
        # 或者 [[False] * n] for _ in range(m)
        # 但是切忌[[False] * n] * m
        # 可变对象不能用乘以一个整数的办法去构造
        visited = [[False for _ in range(n)] for _ in range(m)]

        queue = deque()

        queue.append(start)
        visited[start[0]][start[1]] = True

        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        while queue:
            curr_pos = queue.popleft()
            if curr_pos == destination:
                return True

            for dir_x, dir_y in directions:
                curr_r, curr_c = curr_pos
                while curr_r >= 0 and curr_r < m \
                        and curr_c >= 0 and curr_c < n \
                        and maze[curr_r][curr_c] == 0:
                    dir_x, dir_y = directions[idx]
                    curr_r += dir_x
                    curr_c += dir_y

                curr_r -= dir_x
                curr_c -= dir_y

                if not visited[curr_r][curr_c]:
                    queue.append([curr_r, curr_c])
                    visited[curr_r][curr_c] = True

        return False

    def hasPath_bfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """提前判断“下一个格子”是否能走
        """
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        directions = (-1, 0), (1, 0), (0, -1), (0, 1),

        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = True

        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True

            for dx, dy in directions:
                nr, nc = r, c

                while 0 <= nr + dx < m and 0 <= nc + dy < n and maze[nr + dx][nc + dy] == 0:
                    nr += dx
                    nc += dy

                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append([nr, nc])

        return False


    def hasPath_dfs(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        directions = (-1, 0), (1, 0), (0, -1), (0, 1),

        stack = [start]

        while stack:
            r, c = stack.pop()
            if [r, c] == destination:
                return True

            if visited[r][c]:
                continue
            visited[r][c] = True

            for dx, dy in directions:
                nr, nc = r, c
                # 提前判断，不“撞墙后回退”
                while 0 <= nr + dx < m and 0 <= nc + dy < n and maze[nr + dx][nc + dy] == 0:
                    nr += dx
                    nc += dy

                if not visited[nr][nc]:
                    stack.append([nr, nc])

        return False




