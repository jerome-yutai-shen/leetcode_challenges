# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:36:52 2022

@author: Jerome Yutai Shen

"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res


def permute2(nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])  # 拷贝当前路径
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res


def permute_stack_approach(nums: List[int]) -> List[List[int]]:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]
    result = []
    stack = [[num] for num in nums]
    while stack:
        last = stack.pop()
        if len(last) == len(nums):
            result.append(last)
            continue
        for n in nums:
            if n not in last:
                stack.append(last + [n])
    return result