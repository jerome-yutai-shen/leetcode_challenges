# -*- coding: utf-8 -*-
"""
Created on May 30 01:55:18 2022

@author: Jerome Yutai Shen

"""
from typing import List
from collections import OrderedDict


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(nums: List[int], target: int) -> int:
        # Write your code here
        if not nums:
            return -1
        counter = OrderedDict.fromkeys(nums, 0)
        for num in nums:
            counter[num] = counter.get(num) + 1
            if num == target:
                break
        else:
            return -1

        for num in nums:
            if counter[num] == 1:
                return num
            if num == target:
                break
        return -1


if __name__ == "__main__":
    nums = [1,2,2,1,3,4,4,5,6]
    target = 5
    x1 = {}
    for num in nums:
        x1[num] = x1.get(num, 0) + 1
        if num == target:
            break
    else:
        print(-1)

    x2 = dict.fromkeys(nums, 0)
    for num in nums:
        x2[num] = x2.get(num) + 1
        if num == target:
            break
    else:
        print(-1)