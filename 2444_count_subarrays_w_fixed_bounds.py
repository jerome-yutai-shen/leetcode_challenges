# -*- coding: utf-8 -*-
"""
Created on Apr 17 20:39:18 2023

@author: Jerome Yutai Shen

"""
from typing import List


def count_subarrays(nums: List[int], minK: int, maxK: int) -> int:
    # min_position, max_position: the MOST RECENT positions of minK and maxK.
    # left_bound: the MOST RECENT value outside the range [minK, maxK].
    answer = 0
    min_position = max_position = left_bound = -1

    # Iterate over nums, for each number at index i:
    for i, number in enumerate(nums):
        print(f"begin")
        print(f"i {i}, number {number}, min: {minK} ,max: {maxK}")
        # If the number is outside the range [minK, maxK], update the most recent left_bound.
        if number < minK or number > maxK:
            left_bound = i

        # If the number is minK or maxK, update the most recent position.
        if number == minK:
            min_position = i
        if number == maxK:
            max_position = i
        print(f"left_bound: {left_bound}, min_position: {min_position}, max_position: {max_position}")
        # The number of valid subarrays equals the number of elements between left_bound and
        # the smaller of the two most recent positions.
        delta_count = max(0, min(min_position, max_position) - left_bound)
        print(f"delta_count {delta_count}")
        answer += delta_count
        print(f"end")
    return answer


if __name__ == "__main__":
    nums = [1,3,5,2,3,3,3, 5,6]
    minK = 2
    maxK = 5
    print(f"answer: {count_subarrays(nums, minK, maxK)}")
