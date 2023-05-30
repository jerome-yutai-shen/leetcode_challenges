# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:29:00 2022

@author: Jerome Yutai Shen

"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    n = 0
    for i in range(len(nums)):
        if i > n:
            return False
        n = max(n, nums[i] + i)
    return True