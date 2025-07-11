# -*- coding: utf-8 -*-
"""
Created on Oct 23 03:51:13 2023

@author: Jerome Yutai Shen

"""
# 198 function 分别对nums[:-1], nums[1:], 取最大值

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))