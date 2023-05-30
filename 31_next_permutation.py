# -*- coding: utf-8 -*-
"""
Created on Jun 06 18:29:33 2022

@author: Jerome Yutai Shen

"""
from typing import List, Union


class Solution:
    def nextPermutation(self, nums: List[int]) -> Union[List, None]:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l <= 1:
            return nums

        i, j, k = l - 2, l - 1, l - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]: k -= 1
            nums[i], nums[k] = nums[k], nums[i]

        i, j = j, l - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums