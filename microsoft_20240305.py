# -*- coding: utf-8 -*-
"""
Created on Mar 06 12:19:26 2024

@author: Jerome Yutai Shen

"""
from typing import List, Set


def two_sum(arr: List, target: int) -> bool:
    """
    unsorted
    """
    visited = set()
    for num in arr:
        complement = target - num

        if complement in visited: # 注意 是查看差在不在而不是num在不在
            return True
        visited.add(num)

    return False


if __name__ == "__main__":
    print(two_sum([-1, 2, 0, -2, -3, 3, 5 ], -3))
