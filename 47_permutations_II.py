# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:41:05 2022

@author: Jerome Yutai Shen

"""
from typing import List
import collections


def backtrack(comb, counter, len_nums, results):
    if len(comb) == len_nums:
        # make a deep copy of the resulting permutation,
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