# -*- coding: utf-8 -*-
"""
Created on Jun 25 08:13:44 2025

@author: Jerome Yutai Shen

"""
import heapq
from typing import List
from collections import deque


def dfs_490(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
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


def bfs_490(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """提前判断“下一个格子”是否能走
    """
    m, n = len(maze), len(maze[0])
    visited = [[False] * n for _ in range(m)]
    directions = (-1, 0), (1, 0), (0, -1), (0, 1),

    queue = deque()
    visited[start[0]][start[1]] = True
    queue.append(start)

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


def shortest_distance_505(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    """Dijkstra"""
    m, n = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[float('inf')] * n for _ in range(m)]
    dist[start[0]][start[1]] = 0

    heap = [(0, start[0], start[1])]  # (distance, row, col)

    while heap:
        d, r, c = heapq.heappop(heap)
        if [r, c] == destination:
            return d

        for dx, dy in directions:
            nr, nc = r, c
            steps = 0
            while 0 <= nr + dx < m and 0 <= nc + dy < n and maze[nr + dx][nc + dy] == 0:
                nr += dx
                nc += dy
                steps += 1

            if d + steps < dist[nr][nc]:
                dist[nr][nc] = d + steps
                heapq.heappush(heap, (dist[nr][nc], nr, nc))

    return -1