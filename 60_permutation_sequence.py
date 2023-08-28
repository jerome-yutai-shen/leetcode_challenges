# -*- coding: utf-8 -*-
"""
Created on Jun 08 02:46:43 2022

@author: Jerome Yutai Shen

"""


def getPermutation(n: int, k: int) -> str:
    factorials, nums = [1], ['1']
    for idx in range(1, n):
        # generate factorial system bases 0!, 1!, ..., (n - 1)!
        factorials.append(factorials[idx - 1] * idx)
        # generate nums 1, 2, ..., n
        nums.append(str(idx + 1))

    # fit k in the interval 0 ... (n! - 1)
    k -= 1

    # compute factorial representation of k
    output = []
    for i in range(n - 1, -1, -1):
        idx = k // factorials[i]
        k -= idx * factorials[i]

        output.append(nums[idx])
        del nums[idx]

    return ''.join(output)