# -*- coding: utf-8 -*-
"""
Created on Jul 10 18:21:49 2025

@author: Jerome Yutai Shen

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing