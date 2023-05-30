# -*- coding: utf-8 -*-
"""
Created on Jun 16 05:02:39 2022

@author: Jerome Yutai Shen

"""
from typing import List


def binary_search_any(nums: List[int], target: int) -> int:
    """
    nums is strictly increasing 原题严格递增，没有重复元素
    :param nums:
    :param target:
    :return:
    """

    p_start, p_end = 0, len(nums) - 1

    while p_start + 1 < p_end:
        p_mid = (p_start + p_end) // 2
        if nums[p_mid] == target:
            return p_mid
        elif nums[p_mid] > target: # 就把相等的情况合并
            p_end = p_mid
        else:
            assert nums[p_mid] < target
            p_start = p_mid

    if nums[p_start] == target:
        return p_start

    if nums[p_end] == target:
        return p_end

    return -1


def binary_search_first(nums: List[int], target: int) -> int:
    """
    nums is strictly increasing
    :param nums:
    :param target:
    :return:
    """

    p_start, p_end = 0, len(nums) - 1

    while p_start + 1 < p_end:
        p_mid = (p_start + p_end) // 2
        if nums[p_mid] > target:
            p_end = p_mid
        elif nums[p_mid] < target:
            p_start = p_mid
        else:
            p_end = p_mid

    if nums[p_start] == target:
        return p_start

    if nums[p_end] == target:
        return p_end

    return -1


def binary_search_last(nums: List[int], target: int) -> int:
    """
    nums is strictly increasing
    :param nums:
    :param target:
    :return:
    """

    p_start, p_end = 0, len(nums) - 1

    while p_start + 1 < p_end:
        p_mid = (p_start + p_end) // 2
        if nums[p_mid] > target:
            p_end = p_mid
        elif nums[p_mid] < target:
            p_start = p_mid
        else:
            p_start = p_mid

    if nums[p_end] == target: # 如果输入数组全都是一个数 [1,1,1,1,1] [2, 2]
        return p_end

    if nums[p_start] == target:
        return p_start

    return -1


if __name__ == "__main__":
    nums = [2, 2]
    target = 2
    print(binary_search_any(nums, target))
    print(binary_search_first(nums, target))
    print(binary_search_last(nums, target))