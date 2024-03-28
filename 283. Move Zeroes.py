# -*- coding: utf-8 -*-
"""
Created on Nov 26 18:21:26 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Note that you must do this in-place without making a copy of the array.
        这个版本可以保证最小的“写”次数。
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                if left != right:
                    nums[left] = nums[right]
                left += 1
            right += 1

        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1

    def moveZeroes2(self, nums):
        """
        无法保证写次数最小
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1