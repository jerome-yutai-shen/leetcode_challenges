# -*- coding: utf-8 -*-
"""
Created on Jun 08 04:55:22 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets2(self, nums):
        # write your code here
        nums.sort()
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []

        for i in range(2 ** n, 2 ** (n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output