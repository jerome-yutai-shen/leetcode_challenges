# -*- coding: utf-8 -*-
"""
Created on Nov 26 18:48:08 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = { }

        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = i
            else:
                if abs(i - hm[nums[i]]) <= k:
                    return True
                else:
                    hm[nums[i]] = i

        return False
