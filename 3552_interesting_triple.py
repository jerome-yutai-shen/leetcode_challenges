# -*- coding: utf-8 -*-
"""
Created on Jun 15 11:40:47 2023

@author: Jerome Yutai Shen

"""
from typing import (
    List,
)

class Solution:
    """
    @param nums:
    @return: Returns the existence of an interesting triplet
    """
    def get_fun_tuple(self, nums: List[int]) -> bool:
        larger_behind, mx, mn = [False] * len(nums), min(nums), max(nums)
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] < mx:
                larger_behind[idx] = True
            mx = max(nums[idx], mx)
        for idx in range(len(nums)):
            if nums[idx] > mn and larger_behind[idx]:
                return True
            mn = min(nums[idx], mn)
        return False


