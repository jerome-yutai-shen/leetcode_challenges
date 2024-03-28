# -*- coding: utf-8 -*-
"""
Created on Sep 17 22:42:55 2023

@author: Jerome Yutai Shen

"""
import sys


def twoSumClosest(nums:list):
    nums.sort()
    i, j = 0, len(nums) - 1

    diff = sys.maxsize
    while i < j:
        if nums[i] + nums[j] < 0:
            diff = min(diff, 0 - nums[i] - nums[j])
            i += 1
        else:
            diff = min(diff, nums[i] + nums[j] - 0)
            j -= 1

    return diff


def twoSumClosest_refined(nums:list):
    nums.sort()
    i, j = 0, len(nums) - 1

    diff = sys.maxsize
    while i < j:
        if nums[i] + nums[j] == 0:
            diff = 0
            break
        else:
            diff = min(diff, abs(0 - (nums[i] + nums[j])))
            if nums[i] + nums[j] < 0:
                i += 1
            else:
                j -= 1

    return diff



def findMinSum(arr:list):
    n = len(arr)
    for i in range(1, n):

        # Modified to sort by absolute values
        if (not abs(arr[i - 1]) < abs(arr[i])):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

    Min = sys.maxsize
    x = 0
    y = 0

    for i in range(1, n):

        # Absolute value shows how
        # close it is to zero
        if (abs(arr[i - 1] + arr[i]) <= Min):
            # If found an even close value
            # update min and store the index
            Min = abs(arr[i - 1] + arr[i])
            x = i - 1
            y = i

    return(abs(arr[x] + arr[y]))


def findMinSum2(arr:list):
    n = len(arr)
    arr = sorted(arr, key=lambda x:abs(x))

    Min = sys.maxsize
    x = 0
    y = 0

    for i in range(1, n):

        # Absolute value shows how
        # close it is to zero
        if (abs(arr[i - 1] + arr[i]) <= Min):
            # If found an even close value
            # update min and store the index
            Min = abs(arr[i - 1] + arr[i])
            x = i - 1
            y = i

    return(abs(arr[x] + arr[y]))


if __name__ == "__main__":
    for num in [[1, 60, -10, 70, -80, 85], [-34, 4, 1, -2, 19, -8]]:
        assert(findMinSum(num) == findMinSum2(num))
        assert(twoSumClosest(num) == twoSumClosest_refined(num))
        print(twoSumClosest(num), findMinSum(num))