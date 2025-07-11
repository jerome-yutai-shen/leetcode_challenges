# -*- coding: utf-8 -*-
"""
Created on Jul 09 16:17:01 2025

@author: Jerome Yutai Shen

思路是从gates开始 每一个gate扩散
这道题是所谓的多源头bfs
每个格子最多只会入队一次（只要是空房间且第一次被更新）。
	•	每个点最多检查四个方向 ➜ 常数操作。
	•	所以：时间复杂度是 O(mn)
空间复杂度在最坏情况下Omn 平均的话

"""
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        DIRECTIONS = ((-1, 0), (1, 0), (0, 1), (0, -1))
        m, n = len(rooms), len(rooms[0])
        q_coord = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q_coord.append((i, j)) # 用tuple而不是list

        while q_coord:
            gate = q_coord.popleft()

            for dx, dy in DIRECTIONS:
                nx = gate[0] + dx
                ny = gate[1] + dy
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                    rooms[nx][ny] = rooms[gate[0]][gate[1]] + 1
                    q_coord.append((nx, ny)) # 用tuple而不是list


