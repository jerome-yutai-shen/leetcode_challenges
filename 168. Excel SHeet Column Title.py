# -*- coding: utf-8 -*-
"""
Created on Jul 03 16:52:30 2025

@author: Jerome Yutai Shen

"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber:
            columnNumber -= 1 # 这里的关键是这个
            res += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26

        return res[::-1]
