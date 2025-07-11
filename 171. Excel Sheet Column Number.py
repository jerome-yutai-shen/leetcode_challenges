# -*- coding: utf-8 -*-
"""
Created on Jul 03 17:52:01 2025

@author: Jerome Yutai Shen

"""
class Solution:
    def titleToNumber(self, column_title: str) -> str:
        res = 0
        for char in column_title:
            res = res * 26 + (ord(char) - ord('A') + 1)
        return res