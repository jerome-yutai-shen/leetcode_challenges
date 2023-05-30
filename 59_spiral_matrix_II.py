# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:42:51 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """

    def generate_matrix(self, n: int) -> List[List[int]]:
        # write your code here
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy

        return matrix