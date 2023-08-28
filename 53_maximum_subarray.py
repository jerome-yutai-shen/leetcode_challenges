# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:14:20 2022

@author: Jerome Yutai Shen

"""
from typing import List, Optional
import math


def findBestSubarray(nums: List[int], left: int, right: int) -> Optional[int]:
    # Base case - empty array.
    if left > right:
        return -math.inf

    mid = (left + right) // 2
    curr = best_left_sum = best_right_sum = 0

    # Iterate from the middle to the beginning.
    for i in range(mid - 1, left - 1, -1):
        curr += nums[i]
        best_left_sum = max(best_left_sum, curr)

    # Reset curr and iterate from the middle to the end.
    curr = 0
    for i in range(mid + 1, right + 1):
        curr += nums[i]
        best_right_sum = max(best_right_sum, curr)

    # The best_combined_sum uses the middle element and
    # the best possible sum from each half.
    best_combined_sum = nums[mid] + best_left_sum + best_right_sum

    # Find the best subarray possible from both halves.
    left_half = findBestSubarray(nums, left, mid - 1)
    right_half = findBestSubarray(nums, mid + 1, right)

    # The largest of the 3 is the answer for any given input array.
    return max(best_combined_sum, left_half, right_half)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

    def maxSubArray2(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray