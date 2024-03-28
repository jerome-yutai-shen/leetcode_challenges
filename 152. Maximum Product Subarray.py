# -*- coding: utf-8 -*-
"""
Created on Nov 23 17:51:38 2023

@author: Jerome Yutai Shen

1567. Maximum Length of Subarray With Positive Product

"""
from typing import List, Tuple
from functools import cache


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        @cache
        def dp(idx: int) -> Tuple[int, int]:
            """min or max of subarray product ends with nums[idx]"""
            if idx == 0:
                return nums[idx], nums[idx],

            low, hi = dp(idx - 1) # 问一下前面的人你的最大最小值
            if nums[idx] < 0:
                low, hi = hi, low

            return min(low * nums[idx], nums[idx]), max(hi * nums[idx], nums[idx]),

        return max(dp(idx)[1] for idx in range(len(nums)))
