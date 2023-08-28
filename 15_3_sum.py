# -*- coding: utf-8 -*-
"""
Created on May 24 00:36:39 2022

@author: Jerome Yutai Shen

"""
from typing import List, Set, Tuple


def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            two_sum_2pntr(nums, i, res)
    return res


def two_sum_2pntr(nums: List[int], i: int, res: List[List[int]]):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1


def two_sum_hashset(nums: List[int], i: int, res: List[List[int]]):
    seen = set()
    j = i + 1
    num_i = nums[i]
    while j < len(nums):
        complement = -num_i - nums[j]
        if complement in seen:
            res.append([num_i, nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


def three_sum_nosort(nums: List[int]) -> Set[Tuple[int]]:
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res