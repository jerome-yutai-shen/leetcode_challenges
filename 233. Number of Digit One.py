# -*- coding: utf-8 -*-
"""
Created on Jul 03 19:31:27 2025

@author: Jerome Yutai Shen

"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        digit = 1  # 从个位开始处理
        high, cur, low = n // (10 * digit), (n // digit) % 10, 0

        while n // digit != 0:
            high = n // (digit * 10)
            cur = (n // digit) % 10
            low = n % digit

            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit

            digit *= 10

        return res