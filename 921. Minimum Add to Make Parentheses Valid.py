# -*- coding: utf-8 -*-
"""
Created on Nov 25 17:08:20 2023

@author: Jerome Yutai Shen

"""
class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
