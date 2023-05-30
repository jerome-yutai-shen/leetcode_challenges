# -*- coding: utf-8 -*-
"""
Created on May 24 21:33:55 2022

@author: Jerome Yutai Shen

"""
from typing import List


def three_sum_closest(numbers: List[int], target: int) -> int:
    # write your code here
    sum_three = 0

    if not numbers or len(numbers) < 3:
        return sum_three

    numbers.sort()
    n = len(numbers)

    for i in range(n):
        # first, choose num_i to be fixed
        num_i = numbers[i]

        start, end = i + 1, n - 1
        l, r = start, end

        # then for each l pointer, move r point.
        while l < r:
            while l < r and num_i + numbers[l] + numbers[r] > target:
                r -= 1

                # make sure r and l are not the same.
            if r == l:
                r += 1

            sum_three_smaller = num_i + numbers[l] + numbers[r]
            sum_three_larger = None
            if r + 1 < n:
                sum_three_larger = num_i + numbers[l] + numbers[r + 1]

            if sum_three_larger != None and abs(sum_three_larger - target) <= abs(sum_three_smaller - target):
                sum_three_curr = sum_three_larger
            else:
                sum_three_curr = sum_three_smaller

            if sum_three is None or abs(sum_three_curr - target) <= abs(sum_three - target):
                sum_three = sum_three_curr

            l += 1

    return sum_three


def three_sum_closest2(nums: List[int], target: int) -> int:
    """
    two pointers
    """
    diff = float('inf')
    nums.sort()
    for idx in range(len(nums)):
        lo, hi = idx + 1, len(nums) - 1
        control_var = nums[idx]

        while lo < hi:
            sum_3 = control_var + nums[lo] + nums[hi]
            if abs(target - sum_3) < abs(diff):
                diff = target - sum_3
            if sum_3 < target:
                lo += 1
            else:
                hi -= 1
        if diff == 0:
            break

    return target - diff


def three_sum_closest3(nums: List[int], target: int) -> int:
    """
    binary search
    """
    import bisect
    diff = float('inf')
    nums.sort()
    for idx in range(len(nums)):
        control_var = target - nums[idx]
        for j in range(idx + 1, len(nums)):
            complement = control_var - nums[j]
            hi = bisect.bisect_right(nums, complement, j + 1) #
            lo = hi - 1
            if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                diff = complement - nums[hi]
            if lo > j and abs(complement - nums[lo]) < abs(diff):
                diff = complement - nums[lo]
        if diff == 0:
            break

    return target - diff


def three_sum_closest4(numbers: List[int], target: int):
    # 令狐冲 排序后。 固定一个点，利用双指针的方式，扫描，记录答案即可。
    numbers.sort()
    ans = None
    for idx in range(len(numbers)):
        left, right = idx + 1, len(numbers) - 1
        control_var = numbers[idx]
        while left < right:
            sum_3 = numbers[left] + numbers[right] + control_var
            if ans is None or abs(sum_3 - target) < abs(ans - target):
                ans = sum_3

            if sum_3 < target: # sum_3 ==target 的情况给谁都行
                left += 1
            else:
                right -= 1
        if ans == target:
            break
    return ans


if __name__ == "__main__":
    nums, target = [0, 1, 2], 0
    three_sum_closest3(nums, target)