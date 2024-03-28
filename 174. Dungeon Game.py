# -*- coding: utf-8 -*-
"""
Created on Dec 20 11:17:50 2023

@author: Jerome Yutai Shen

"""
from typing import List
import sys


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        hp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)] # 血量无上限

        hp[m][n - 1] = hp[m - 1][n] = 1

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                hp[y][x] = max(1, min(hp[y + 1][x], hp[y][x + 1]) - dungeon[y][x])

        return hp[0][0]