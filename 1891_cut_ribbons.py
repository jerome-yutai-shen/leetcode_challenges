# -*- coding: utf-8 -*-
"""
Created on Aug 31 16:24:29 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    # def maxLength(self, ribbons: List[int], k: int) -> int:
    #     ribbons.sort()
    #     min_len, max_len = 0, ribbons[-1]
    #     while min_len <= max_len:
    #         count = self.count_ribbon_cuts(ribbons[::-1], max_len) # 错！
    #         mid_len = (min_len + max_len + 1) // 2
    #         if count  < k:
    #             min_len = mid_len
    #         else:
    #             max_len = mid_len
    #     return min_len

    def count_ribbon_cuts(self, a: list, max_length: int) -> int:
        count = 0
        for x in a:
            if x < max_length:
                break
            count += x // max_length
        return count

    def maxLength(self, ribbons: List[int], k: int) -> int:
        ribbons.sort()
        left, right = 0, ribbons[-1]
        while left < right:
            mid = (left + right + 1) // 2
            cnt = self.count_ribbon_cuts(ribbons[::-1], mid)
            if cnt >= k:
                left = mid
            else:
                right = mid - 1
        return left