# -*- coding: utf-8 -*-
"""
Created on Nov 24 10:16:53 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum > target:
                right -= 1
            elif _sum < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return [-1, -1]