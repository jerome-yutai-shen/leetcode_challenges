# -*- coding: utf-8 -*-
"""
Created on Jul 05 23:29:59 2025

@author: Jerome Yutai Shen

双指针的标准写法（懒加载）

"""
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.col = 0

    def hasNext(self) -> bool:
        # 跳过空行或走到某行尾部时，移动到下一行
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.vec)

    def next(self) -> int:
        # 先调用 hasNext 确保位置合法
        if self.hasNext():
            val = self.vec[self.row][self.col]
            self.col += 1
            return val