# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:13:25 2022

@author: Jerome Yutai Shen

"""
from typing import List


def jump(a: List[int]) -> int:
    # write your code here
    n = len(a)
    max_pos, end, step = 0, 0, 0
    for idx in range(n - 1):
        if max_pos >= idx:
            max_pos = max(max_pos, idx + a[idx])
            if idx == end:
                end = max_pos
                step += 1
    return step