# -*- coding: utf-8 -*-
"""
Created on Dec 26 16:06:10 2023

@author: Jerome Yutai Shen

"""
from typing import List
import numpy as np


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Calculate the median
        nums.sort()
        n = len(nums)
        _median = int(np.median(nums)) # nums[n // 2]
        # Calculate the sum of absolute differences from the median
        moves = 0
        for num in nums:
            moves += abs(num - _median)

        return moves
