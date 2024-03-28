# -*- coding: utf-8 -*-
"""
Created on Nov 23 18:24:10 2023

@author: Jerome Yutai Shen

152. Maximum Product Subarray

"""
from functools import cache
from typing import List, Tuple


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        """
        O(n), O(n)
        """

        @cache
        def dp(idx: int) -> Tuple[int, int]:
            """Max length of positive/negative product array ends"""
            if idx < 0 or nums[idx] == 0:
                return 0, 0

            p, n = dp(idx - 1)
            if nums[idx] > 0:
                return p + 1, n + 1 if n else 0
            else:
                return n + 1 if n else 0, p + 1

        return max(dp(idx)[0] for idx in range(len(nums)))