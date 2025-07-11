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

def search九章模版(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (right + left) // 2

        # Case 1: find target
        if nums[mid] == target:
            return mid

        # Case 2: subarray on mid's left is sorted
        elif nums[mid] > nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Case 3: subarray on mid's right is sorted.
        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right

    return -1