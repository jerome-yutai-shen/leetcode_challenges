# -*- coding: utf-8 -*-
"""
Created on May 31 10:55:40 2023

@author: Jerome Yutai Shen

"""
from typing import List


def max_subsequence(a: List[int], diff = 1):
    count = {}
    for num in a:
        count[num] = count.get(num, 0) + 1

    max_len=0
    for num in count:
        max_len = max(max_len, count[num] + count.get(num + diff, 0))
    return max_len


if __name__ == "__main__":
    print(max_subsequence([1,3,2,2,5,2,3,7]))