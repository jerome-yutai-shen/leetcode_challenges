# -*- coding: utf-8 -*-
"""
Created on Oct 03 02:17:27 2023

@author: Jerome Yutai Shen

"""
from collections import defaultdict
from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    counts = defaultdict(int)
    ans = 0

    for num in nums:
        ans += counts[num]
        counts[num] += 1

    return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]

