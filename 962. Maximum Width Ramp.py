# -*- coding: utf-8 -*-
"""
Created on Dec 18 21:33:27 2023

@author: Jerome Yutai Shen

2863
"""
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []
        for idx in range(n):
            if not stk or nums[idx] <= nums[stk[-1]]:
                stk.append(idx)

        ret = 0
        for idx in range(n - 1, -1, -1):
            # print(idx, stk)
            while stk and nums[stk[-1]] <= nums[idx]:
                ret = max(ret, idx - stk[-1])
                stk.pop()

        return ret


def f2863(nums: List[int]) -> int:
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
        while stk and nums[idx] < nums[stk[-1]]:
            ret = max(ret, idx - stk[-1] + 1)
            stk.pop()

    return ret


def f962(nums: List[int]) -> int:
    """
    i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
    """
    n = len(nums)
    stk = []
    for idx in range(n):
        if not stk or nums[idx] <= nums[stk[-1]]:
            stk.append(idx)

    ret = 0
    for idx in range(n - 1, -1, -1):
        while stk and nums[idx] >= nums[stk[-1]]:
            ret = max(ret, idx - stk[-1])
            stk.pop()

    return ret
