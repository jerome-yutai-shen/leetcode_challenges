# -*- coding: utf-8 -*-
"""
Created on Feb 12 11:50:33 2024

@author: Jerome Yutai Shen

"""
def count_h_v(nums: list) -> int:
    count = 0
    if not nums:
        return count

    for idx in range(1, len(nums) - 1):

        if nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]:
            count += 1
        elif nums[idx] < nums[idx - 1] and nums[idx] < nums[idx + 1]:
            count += 1
        elif nums[idx] == nums[idx + 1]: #遇到跟下一个相等，就把自身替换为前一个，前一个已经被计数
            nums[idx] = nums[idx - 1]

    return count