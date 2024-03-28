# -*- coding: utf-8 -*-
"""
Created on Nov 12 01:26:23 2023

@author: Jerome Yutai Shen

"""
from typing import List


def printPrevSmaller(arr: List[int]):
    """
    O(n), O(n)
    """
    S = []
    ans = []

    # Traverse all array elements
    for num in arr:
        while (S and S[-1] >= num):
            S.pop()

        if not S:
            ans.append("_")
        else:  # Else print the nearest
            # smaller element
            ans.append(S[-1])

        S.append(num)
        # print(f"num: {num}, S: {S}")
    return ans


if __name__ == "__main__":
    arr = [1, 6, 10, 4, 2, 5]
    _1 = printPrevSmaller(arr)
    arr = [1, 6, 4, 10, 2, 5]
    _2 = printPrevSmaller(arr)
    arr = [1, 3, 0, 2, 5]
    _3 = printPrevSmaller(arr)