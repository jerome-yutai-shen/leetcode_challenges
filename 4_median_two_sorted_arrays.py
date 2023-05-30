# -*- coding: utf-8 -*-
"""
Created on Jun 07 20:08:37 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # write your code here
        # write your code here
        len_a, len_b = len(nums1), len(nums2)
        if (len_a + len_b) % 2 == 1:
            return self.find_kth(nums1, nums2, (len_a + len_b) // 2 + 1)
        else:
            left = self.find_kth(nums1, nums2, (len_a + len_b) // 2)
            right = self.find_kth(nums1, nums2, (len_a + len_b) // 2 + 1)
            return (left + right) / 2

    def find_kth(self, A, B, k):
        if len(A) == 0:
            left, right = B[0], B[-1]
        elif len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0], B[0]), max(A[-1], B[-1])
        while left + 1 < right:
            mid = (left + right) // 2
            count1 = self.helper(A, mid)
            count2 = self.helper(B, mid)
            if count1 + count2 < k:
                left = mid
            else:
                right = mid
        count1 = self.helper(A, left)
        count2 = self.helper(B, left)
        if count1 + count2 >= k:
            return left
        else:
            return right

    def helper(self, array, flag):
        if len(array) == 0:
            return 0
        left, right = 0, len(array) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= flag:
                left = mid
            else:
                right = mid
        if array[right] <= flag:
            return right + 1
        if array[left] <= flag:
            return left + 1
        return 0
