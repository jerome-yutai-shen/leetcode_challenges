# -*- coding: utf-8 -*-
"""
Created on Jul 05 21:32:09 2025

@author: Jerome Yutai Shen

"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        解法一：位运算（最高效）

        关键思想：

        一个数如果是 2 的幂，它的二进制表示中只有一个 1，例如：
            •	1 => 0001
            •	2 => 0010
            •	4 => 0100
            •	8 => 1000
        """
        return n > 0 and (n & (n - 1)) == 0