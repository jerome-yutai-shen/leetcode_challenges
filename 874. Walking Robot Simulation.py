# -*- coding: utf-8 -*-
"""
Created on Nov 22 14:04:38 2023

@author: Jerome Yutai Shen

"""
from typing import List


CONST_DX = (0, 1, 0, -1)
CONST_DY = (1, 0, -1, 0)


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans