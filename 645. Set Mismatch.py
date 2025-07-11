# -*- coding: utf-8 -*-
"""
Created on Jul 10 01:16:30 2025

@author: Jerome Yutai Shen

"""
from collections import Counter


class Solution:
    """O(n), O(n)"""
    def findErrorNums1(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = [None] * 2
        for num in range(1, len(nums) + 1):
            if num not in count:
                res[1] = num  # missing
            elif count[num] == 2:
                res[0] = num  # duplicated
        return res

    def findErrorNums(self, nums: List[int]) -> List[int]:
        """O(n) O(1)"""
        n = len(nums)
        total = n * (n + 1) // 2
        actual_sum = sum(nums)
        actual_set_sum = sum(set(nums))
        duplicate = actual_sum - actual_set_sum
        missing = total - actual_set_sum
        return [duplicate, missing]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        """原地标记 O(n) O(1)"""
        dup = -1
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                dup = abs(num)  # 第二次访问，说明是重复的
            else:
                nums[index] *= -1  # 第一次访问，做标记

        # 找缺失的数（没有被标记为负数）
        missing = -1
        for i, val in enumerate(nums):
            if val > 0:
                missing = i + 1
                break

        return [dup, missing]