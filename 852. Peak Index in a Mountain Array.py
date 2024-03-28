# -*- coding: utf-8 -*-
"""
Created on Nov 23 11:11:48 2023

@author: Jerome Yutai Shen

"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """O(logn), O(1)"""
        if not arr:
            return -1

        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            print(mid)
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        if arr[start] > arr[end]:
            return start

        return end