# -*- coding: utf-8 -*-
"""
Created on Jun 03 21:05:45 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p_start = 0

        for p_end in range(1, len(nums)):
            if nums[p_end] != nums[p_start]:
                p_start += 1
                nums[p_start] = nums[p_end]

        return p_start + 1


if __name__ == "__main__":
    pass