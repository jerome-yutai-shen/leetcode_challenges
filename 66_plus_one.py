# -*- coding: utf-8 -*-
"""
Created on Jun 08 03:09:56 2022

@author: Jerome Yutai Shen

"""
from typing import List



def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    # move along the input array starting from the end
    for idx in range(n - 1, -1, -1):
        # idx = n - 1 - i
        # set all the nines at the end of array to zeros
        if digits[idx] == 9:
            digits[idx] = 0
        # here we have the rightmost not-nine
        else:
            # increase this rightmost not-nine by 1
            digits[idx] += 1
            # and the job is done
            return digits

    # we're here because all the digits are nines
    return [1] + digits


if __name__ == "__main__":
    digits = [2, 2, 3, 1]
    print(plusOne(digits))