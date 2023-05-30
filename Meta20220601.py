# -*- coding: utf-8 -*-
"""
Created on Jun 01 15:26:34 2022

@author: Jerome Yutai Shen

"""
from typing import List


def func(nums: List[int], target: int) -> List:
    """
    case 1 : find all the element pairs in nums, which sums equal to the target
    case 2: find  all the triple element
    :param nums: [1, 2, 2, 3, 4]
    [2,2,3,1,4]
    :param target:  6

    :return: [2, 4]
    """

    visited = set()
    results = []

    for num in nums:
        visited.add(num) # {1, 2}
        if target - num in nums:
            results.append([num, target])

    return results


def power(a: int, b: int) -> int:
    """
    :param a:  positive int
    :param b:  positive int
    :return:
    b = 6 (a ** 3) ** 2
    b = 16 (a ** 4) ** 4
    a = 3, b = 8
    """

    pow_a_b = 1
    while b > 0:
        pow_a_b *= a
        b -= 1
    return pow_a_b


def power2(a, b):
    if b == 2:
        return a * a
    if b == 1:
        return a

    power2(a, b // 2)
    return

