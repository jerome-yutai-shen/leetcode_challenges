# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:41:05 2022

@author: Jerome Yutai Shen

"""
from typing import List
import collections


def backtrack(comb, counter, len_nums, results):
    if len(comb) == len_nums:
        # make a shallow copy of the resulting permutation,
        # since the permutation would be backtracked later.
        results.append(list(comb))
        return

    for num in counter:
        if counter[num] > 0:
            # add this number into the current combination
            comb.append(num)
            counter[num] -= 1
            # continue the exploration
            backtrack(comb, counter, len_nums, results)
            # revert the choice for the next exploration
            comb.pop()
            counter[num] += 1


def permuteUnique(nums: List[int]) -> List[List[int]]:
    results = []
    backtrack([], collections.Counter(nums), len(nums), results)
    return results


def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    used = [False] * len(nums)
    nums.sort()

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue  # 去重的关键：同层中避免重复使用相同元素
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return res