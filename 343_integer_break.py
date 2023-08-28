# -*- coding: utf-8 -*-
"""
Created on Jul 11 12:18:22 2023

@author: Jerome Yutai Shen

"""

def integerBreak(n: int) -> int:
    special_factors = (2, 3, 4)

    if n in special_factors:
        return dict(zip(special_factors, (1, 2, 4))).get(n)

    ans = 1
    factors = []

    while n >= 5:
        factors.append(3)
        n -= 3

    if n in special_factors:
        factors.append(n)
        n -= n

    for factor in factors:
        ans *= factor

    return ans

