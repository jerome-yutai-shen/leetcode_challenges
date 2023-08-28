# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:01:49 2022

@author: Jerome Yutai Shen

"""


def power_int(x: float, n: int) -> float:
    if x == 0.0:
        return x
    res = 1
    if n < 0:
        x, n = 1 / x, -n

    while n:
        if n & 1:
            res *= x
        n >>= 1
        x *= x

    return res