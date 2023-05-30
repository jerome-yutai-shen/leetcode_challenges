# -*- coding: utf-8 -*-
"""
Created on Jun 07 02:15:11 2022

@author: Jerome Yutai Shen

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


if __name__ == "__main__":
    nums, target = [1, 3, 5, 6], 2
    search_insert(nums, target)