# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:56:41 2022

@author: Jerome Yutai Shen

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        from math import factorial
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)