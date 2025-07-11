# -*- coding: utf-8 -*-
"""
Created on Jun 07 02:15:11 2022

@author: Jerome Yutai Shen

这个例子当中 如果right = pivot或者left = pivot就会出现死循环
所以不如用九章模版
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return left

def searchInsert九章(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    left, right = 0, len(nums) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # 后处理：判断 target 应该插入到哪一边
    if nums[left] >= target:
        return left
    elif nums[right] >= target:
        return right
    else:
        return right + 1


def searchInsert_九章2(nums, target):
    if not nums:
        return 0  # 插入在第一个位置

    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid

    # 后处理阶段：找第一个 >= target 的位置
    if nums[start] >= target:
        return start
    elif nums[end] >= target:
        return end
    else:
        return end + 1


if __name__ == "__main__":
    nums, target = [1, 3, 5, 6], 2
    search_insert(nums, target)