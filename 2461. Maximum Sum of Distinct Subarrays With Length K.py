# -*- coding: utf-8 -*-
"""
Created on Feb 13 02:47:50 2024

@author: Jerome Yutai Shen

"""
from typing import List
from collections import defaultdict


def maximumSubarraySum(nums: List[int], k: int) -> int:
    """
    两点优化
    用cum_sum累加 同时不断减去左边在k之外的元素
    只维护一个计数dict，而不是每次生成新的Counter或者set。
    去掉频数为零的元素key。
    """
    running_sum = 0
    num_freq = defaultdict(int)
    max_sum = 0

    for i in range(len(nums)):
        # update running sum & num_freq
        num_freq[nums[i]] += 1
        running_sum += nums[i]

        # keep the window size k
        if i >= k: # k is 3, when idx == 3, remove nums[0]
            running_sum -= nums[i - k]
            num_freq[nums[i - k]] -= 1

            if num_freq[nums[i - k]] == 0:
                del num_freq[nums[i - k]]

        # only update max_sum if no repeated num in num_freq
        if len(num_freq) == k:
            max_sum = max(max_sum, running_sum)

    return max_sum