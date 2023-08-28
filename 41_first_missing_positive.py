# -*- coding: utf-8 -*-
"""
Created on Jun 07 13:33:42 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case.
        if 1 not in nums:
            return 1

        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain
        # only positive numbers.
        for idx in range(n):
            if nums[idx] <= 0 or nums[idx] > n:
                nums[idx] = 1

        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array.
        # If nums[2] is positive - number 2 is missing.
        for idx in range(n):
            a = abs(nums[idx])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        # Now the index of the first positive number
        # is equal to first missing positive.
        for idx in range(1, n):
            if nums[idx] > 0:
                return idx

        if nums[0] > 0:
            return n

        return n + 1