# -*- coding: utf-8 -*-
"""
Created on Oct 23 20:57:20 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums.sort()

        for i in range(0, len(nums) - 1, 3):
            if nums[i] == nums[i + 1]:
                continue
            else:
                return nums[i]

        return nums[len(nums) - 1]


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2