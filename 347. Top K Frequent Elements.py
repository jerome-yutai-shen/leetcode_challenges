# -*- coding: utf-8 -*-
"""
Created on Dec 19 14:44:04 2023

@author: Jerome Yutai Shen

"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)