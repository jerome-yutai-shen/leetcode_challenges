# -*- coding: utf-8 -*-
"""
Created on Jun 25 07:47:35 2025

@author: Jerome Yutai Shen

"""
import heapq
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
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