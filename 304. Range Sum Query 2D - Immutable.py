# -*- coding: utf-8 -*-
"""
Created on Nov 26 23:27:11 2023

@author: Jerome Yutai Shen

221. Maximal Square
"""
from typing import List


class NumMatrix花花:

    def __init__(self, matrix: List[List[int]]):
        self._sums = []
        if matrix:
            m = len(matrix)
            n = len(matrix[0])
            self._sums = [[0] * (n + 1) for _ in range(m + 1)]

            for idx in range(1, m + 1):
                for j in range(1, n + 1):
                    self._sums[idx][j] = matrix[idx - 1][j - 1] \
                                         + self._sums[idx - 1][j] \
                                         + self._sums[idx][j - 1] \
                                         - self._sums[idx - 1][j - 1]
        print(self._sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sums[row2 + 1][col2 + 1] \
            - self._sums[row2 + 1][col1] \
            - self._sums[row1][col2 + 1] \
            + self._sums[row1][col1]


class NumMatrix:
    table = [[]]

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        N = len(matrix)
        M = len(matrix[0])
        table = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        for i in range(0, N):
            for j in range(0, M):
                table[i + 1][j + 1] = table[i + 1][j] + table[i][j + 1] - table[i][j] + matrix[i][j]
        self.table = table
        print(table)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if len(self.table) == 0 or len(self.table[0]) == 0:
            return 0
        return (self.table[row2 + 1][col2 + 1] + self.table[row1][col1] -
                self.table[row1][col2 + 1] - self.table[row2 + 1][col1])
