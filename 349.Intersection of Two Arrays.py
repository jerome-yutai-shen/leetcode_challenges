# -*- coding: utf-8 -*-
"""
Created on Mar 10 15:08:55 2024

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))