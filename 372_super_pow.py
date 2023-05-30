# -*- coding: utf-8 -*-
"""
Created on Jun 10 04:39:10 2022

@author: Jerome Yutai Shen

"""
from typing import List


def mod(x):
    return x % 1337


class Solution:
    """
    @param a: the given number a
    @param b: the given array
    @return: the result
    """
    def superPow(self, a: int, b: List[int]) -> int:
        # Write your code here
        if a == 0:
            return 0
        ans = 1

        for num in b:
            ans = mod(mod(ans ** 10) * mod(a ** num))
        return ans