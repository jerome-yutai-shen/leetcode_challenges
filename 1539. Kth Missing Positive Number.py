# -*- coding: utf-8 -*-
"""
Created on Nov 26 00:00:21 2023

@author: Jerome Yutai Shen

"""
from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2
        # If number of positive integers
        # which are missing before arr[pivot]
        # is less than k -->
        # continue to search on the right.

        # 正常[1,2,3,4,5],现在是[2,3,4,7,11]，4的位置是2 arr[2] - 2 还要再- 1， 因为是0开始
        # 或者不如说 arr[2]应该先减一，这样自然数计数方式才能适应（通过平移）python下标方式，
        # 如果像MATLAB那样1开始， 4的位置就是3 arr[3] - 3 等于1
        if arr[pivot] - 1 - pivot < k:

            left = pivot + 1
        # Otherwise, go left.
        else:
            right = pivot - 1

    # At the end of the loop, left = right + 1,
    # and the kth missing is in-between arr[right] and arr[left].
    # The number of integers missing before arr[right] is
    # arr[right] - right - 1 -->
    # the number to return is
    # arr[right] + k - (arr[right] - right - 1) = k + left
    return left + k


if __name__ == "__main__":
    arr, k = [2,3,4,7,11], 5
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot = (left + right) // 2
        # If number of positive integers
        # which are missing before arr[pivot]
        # is less than k -->
        # continue to search on the right.
        if arr[pivot] - pivot - 1 < k:
            left = pivot
        # Otherwise, go left.
        else:
            right = pivot
