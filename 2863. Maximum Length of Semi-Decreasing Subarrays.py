# -*- coding: utf-8 -*-
"""
Created on Dec 18 21:24:02 2023

@author: Jerome Yutai Shen

962一样，单调栈
"""
from typing import List

def maxSubarrayLength(nums: List[int]):
    """
    first element is strictly greater than its last element.
    """
    n = len(nums)
    stk = []
    for idx in range(n):
        if not stk or nums[idx] > nums[stk[-1]]:
            stk.append(idx)

    ret = 0
    for idx in range(n - 1, -1, -1):
        # print(idx, stk)
        while stk and nums[stk[-1]] > nums[idx]:
            ret = max(ret, idx - stk[-1] + 1)
            stk.pop()

    return ret