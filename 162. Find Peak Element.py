# -*- coding: utf-8 -*-
"""
Created on Nov 26 16:24:23 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    """
    不能套用九章l + 1 < r。 O(log2 n), O(1)
    """
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            elif nums[mid] == nums[mid + 1]:
                l = mid
            else:
                l = mid + 1 # 关键

        return l

    def findPeakElement2(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            elif nums[mid] == nums[mid + 1]: # 也可以
                l = mid
            else:
                l = mid + 1

        return l
