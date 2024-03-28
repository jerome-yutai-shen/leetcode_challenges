# -*- coding: utf-8 -*-
"""
Created on Nov 25 15:46:02 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans

        return ""
