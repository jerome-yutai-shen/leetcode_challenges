# -*- coding: utf-8 -*-
"""
Created on Jul 11 00:03:07 2023

@author: Jerome Yutai Shen

"""

def subassy_sum(nums: list, k: int) -> int:
    """
    任意 从 i到j的和 可以用 cum_sum(j) - cum_sum(i)
    [3, 4, 7, 2, -3, 1, 4, 2], k = 7
    sum(nums[5:8]) = cum_sum(nums[0:8]) - cum_sum(nums[0:5])
    """
    count = 0
    cum_sum = 0
    hashmap = {0: 1}
    for _ in nums:
        cum_sum += _
        if cum_sum - k in hashmap:
            count += hashmap.get(cum_sum - k)
        hashmap[cum_sum] = hashmap.get(cum_sum, 0) + 1

    return count

