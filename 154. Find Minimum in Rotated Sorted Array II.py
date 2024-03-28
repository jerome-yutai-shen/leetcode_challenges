# -*- coding: utf-8 -*-
"""
Created on Nov 25 01:53:19 2023

@author: Jerome Yutai Shen

153 unique
154 duplicates
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]

    def findMin153(self, nums):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        print(start, end)
        return min(nums[start], nums[end])

    def findMin154(self, nums: List[int]) -> int:
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # risk of overflow: pivot = (low + high) // 2
            # Case 1):
            if nums[mid] > nums[end]:
                start = mid
                # alternative: high = pivot - 1
                # too aggressive to move the `high` index,
                # it won't work for the test case of [3, 1, 3]
            # Case 2):
            elif nums[mid] < nums[end]:
                end = mid
            # Case 3):
            else:
                end -= 1 # 关键区别在于这一步。只可以挪动end指针一步。
        # the 'low' and 'high' index converge to the inflection point.
        return min(nums[start], nums[end])


if __name__ == "__main__":
    _1 = Solution()
    nums = [1, 3, 3]
    print(_1.findMin154(nums))
    nums = [1, 3, 5]
    print(_1.findMin154(nums))
    nums = [3, 3, 1, 3]
    print(_1.findMin154(nums))
    nums = [3, 1, 3]
    print(_1.findMin154(nums))