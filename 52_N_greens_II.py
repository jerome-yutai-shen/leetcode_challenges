# -*- coding: utf-8 -*-
"""
Created on Jun 07 19:25:33 2022

@author: Jerome Yutai Shen

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        # write your code here
        self.ans = 0
        self.dfs(n, [])
        return self.ans

    def dfs(self, n, cols):
        row = len(cols)
        if row == n:
            self.ans += 1
            return
        for col in range(n):
            if self.isValid(n, cols, row, col) == False:
                continue
            cols.append(col)
            self.dfs(n, cols)
            cols.pop()

    def isValid(self, n, cols, row, col):
        for r, c in enumerate(cols):
            if r + c == row + col or r - c == row - col:
                return False
            if col == c:
                return False
        return True