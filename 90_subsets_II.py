# -*- coding: utf-8 -*-
"""
Created on Jun 08 11:09:47 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        output_refined = []
        for _ in output:
            _.sort()
            if _ not in output_refined:
                output_refined.append(_)

        return output_refined