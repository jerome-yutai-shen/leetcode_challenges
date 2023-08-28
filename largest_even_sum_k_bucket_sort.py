# -*- coding: utf-8 -*-
"""
Created on Apr 01 16:56:31 2022

@author: Jerome Yutai Shen

桶排序

"""

from typing import List


def EvenSumK(nums_array: List, k: int):

    if not nums_array or k > len(nums_array):
        return -1

    even_array = []
    odd_array = []
    nums_array.sort(reverse = True)


    for num in nums_array:
        if num % 2 == 0:
            even_array.append(num)
        else:
            odd_array.append(num)

    num_even, num_odd = len(even_array), len(odd_array)
    pntr_even, pntr_odd = 0, 0
    max_evensum = 0

    while k > 0:
        # print(k)
        if k % 2 == 1:
            if (num_even > 0):
                max_evensum += even_array[pntr_even]
                pntr_even += 1
                k -= 1
            else:
                return -1
        else:
            if pntr_even < num_even - 1 and pntr_odd < num_odd - 1:
                if even_array[pntr_even] + even_array[pntr_even + 1] < odd_array[pntr_odd] + odd_array[pntr_odd + 1]:
                    max_evensum += odd_array[pntr_odd] + odd_array[pntr_odd + 1]
                    pntr_odd += 2
                else:
                    max_evensum += even_array[pntr_even] + even_array[pntr_even + 1]
                    pntr_even += 2

            elif pntr_even < num_even - 1:
                max_evensum += even_array[pntr_even] + even_array[pntr_even + 1]
                pntr_even += 2
            elif pntr_odd < num_odd - 1:
                max_evensum += odd_array[pntr_odd] + odd_array[pntr_odd + 1]
                pntr_odd += 2

            k -= 2

    return max_evensum


if __name__ == "__main__":

    for A, K in [[[4,9,8,2,6], 3],
                 [[5, 6, 3, 4, 2], 5],
                 [[7, 7, 7 ,7, 7], 1],
                 [[10000], 2],
                 [[2, 3, 3, 5, 5], 3]]:
        print(f"max_evensum: {EvenSumK(A, K)}")