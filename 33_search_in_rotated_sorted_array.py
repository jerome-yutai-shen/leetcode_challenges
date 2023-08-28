# -*- coding: utf-8 -*-
"""
Created on Jun 08 05:22:49 2022

@author: Jerome Yutai Shen

"""
"""

1, 2, 3, 4, 5, 6, 7
2, 3, 4, 5, 6, 7, 1 
3, 4, 5, 6, 7, 1, 2
4, 5, 6, 7, 1, 2, 3 
5, 6, 7, 1, 2, 3, 4
6, 7, 1, 2, 3, 4, 5
7, 1, 2, 3, 4, 5, 6

when nums[mid] > nums[end]
it must be also > nums[start]

"""
from typing import List


def search(nums: List[int], target: int) -> int:

    if not nums:
        return -1

    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] >= nums[start]:
            if nums[start] <= target <= nums[mid]:
                end = mid
            else:
                start = mid
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid
            else:
                end = mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end

    return -1