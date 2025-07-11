# -*- coding: utf-8 -*-
"""
Created on Jul 01 23:20:06 2025

@author: Jerome Yutai Shen

"""
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    left = 0
    sub_sum = 0
    max_len = n + 1

    for right in range(n):
        sub_sum += nums[right]
        while sub_sum >= target and left <= right:
            max_len = min(max_len, right - left + 1)
            sub_sum -= nums[left]
            left += 1

    return 0 if max_len == n + 1 else max_len


