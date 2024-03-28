# -*- coding: utf-8 -*-
"""
Created on Aug 31 16:40:41 2023

@author: Jerome Yutai Shen

整数数组，每个元素在1到1000之间。
没有0或负数

"""
from typing import List

# brute-force
def twoSumLessThanK1(self, nums: List[int], k: int) -> int:
    """
    O(n ** 2), O(1)
    """
    answer = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum < k:
                answer = max(answer, sum)
    return answer

def twoSumLessThanK(nums: List[int], k: int) -> int:
    answer = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum < k:
                answer = max(answer, sum)
    return answer

# two pointers
def twoSumLessThanK2(nums: List[int], k: int) -> int:
    """
    Time Complexity:
    O(nlogn) to sort the array. The two pointers approach itself is O(n), so the time complexity would be linear if the input is sorted.
    Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.
    """
    nums.sort()
    answer = -1
    left = 0
    right = len(nums) -1
    while left < right:
        sum = nums[left] + nums[right]
        if (sum < k):
            answer = max(answer, sum)
            left += 1
        else:
            right -= 1
    return answer


# binary search
import bisect
def twoSumLessThanK3(nums: List[int], k: int) -> int:
    """
    Time Complexity:
    O(nlogn) to sort the array. The two pointers approach itself is O(n), so the time complexity would be linear if the input is sorted.
    Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.
    """
    answer = -1
    nums.sort()
    for i in range(len(nums)):
        j = bisect.bisect_left(nums, k - nums[i], i + 1) - 1
        if nums[i] > k:
            break
        if j > i:
            answer = max(answer, nums[i] + nums[j])
    return answer


if __name__ == "__main__":
    nums, k = [34, 23, 1, 24, 75, 33, 54, 8], 60
    print(twoSumLessThanK3(nums, k))

    nums, k = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944], 200
    print(twoSumLessThanK3(nums, k))

    nums, k = [1, 1, 1, 1, 10, 10, 10, 8], 14
    print(twoSumLessThanK3(nums, k))