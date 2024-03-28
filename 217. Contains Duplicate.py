# -*- coding: utf-8 -*-
"""
Created on Nov 26 18:42:59 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """O(n), O(n)"""
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """O(nlogn), O(1)"""

        nums.sort()
        for idx in range(len(nums) - 1):
            if (nums[idx] == nums[idx + 1]):
                return True

        return False

