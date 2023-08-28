# -*- coding: utf-8 -*-
"""
Created on Jun 01 15:53:17 2022

@author: Jerome Yutai Shen

"""
from typing import List, Set


def two_sum_1(nums: List[int], target: int) -> List[int]:
    res = [-1, -1]
    unique_nums = dict()
    for idx, num in enumerate(nums):
        completment = target - num
        if completment in unique_nums:        
            return sorted([idx, unique_nums.get(completment)])
        else:
            unique_nums[num] = idx
    else:
        return res


def two_sum(nums: List[int], target: int) -> Set:
    """
    case 1 : find all the element pairs in nums, which sums equal to the target
    case 2: find  all the triple element
    :param nums: [1, 2, 2, 3, 4]
    [2,2,3,1,4]
    :param target:  6

    :return: [2, 4]
    """

    visited = set()
    results = set()

    for num in nums:
        complement = target - num
        if complement in visited:
            results.add(tuple(sorted(([complement, num])))) # num follows complement
        visited.add(num)

    print(results, "\n")
    return results


def two_sum2(nums: List[int], target: int) -> Set:
    """
    case 1 : find all the element pairs in nums, which sums equal to the target
    case 2: find  all the triple element
    :param nums: [1, 2, 2, 3, 4]
    [2,2,3,1,4]
    :param target:  6

    :return: [2, 4]
    """

    results = set()
    # value_idx = sorted([(num, idx) for idx, num in enumerate(nums)])
    sorted_nums = sorted(nums) # O(nlogn)

    p_left, p_right = 0, len(nums) - 1
    while p_left < p_right:
        if sorted_nums[p_left] + sorted_nums[p_right] < target:
            p_left += 1
        elif sorted_nums[p_left] + sorted_nums[p_right] > target:
            p_right -= 1
        else:
            assert sorted_nums[p_left] + sorted_nums[p_right] == target
            results.add((sorted_nums[p_left], sorted_nums[p_right],))

            p_left += 1
            p_right -= 1

    print(results, "\n")

    return results


def two_sum_leetcode(nums: List[int], target: int) -> List:
    hashmap = { }
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


if __name__ == "__main__":
    two_sum2([1, 2, 2, 3, 3, 4], 6)
    two_sum2([3, 2, 4, 4, 6, 2, 9, -1], 8)