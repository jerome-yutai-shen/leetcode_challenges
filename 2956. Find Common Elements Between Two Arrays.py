# -*- coding: utf-8 -*-
"""
Created on Feb 12 12:12:28 2024

@author: Jerome Yutai Shen

"""
from typing import List


def findIntersectionValues2(nums1: List[int], nums2: List[int]) -> List[int]:
    return [sum(x in nums2 for x in nums1), sum(x in nums1 for x in nums2)]


def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    freq1 = [0] * 101
    freq2 = [0] * 101

    out = [0] * 2

    for n in nums1:
        freq1[n] += 1

    for n in nums2:
        freq2[n] += 1

    fout = 0
    for n in nums1: # nums1中的值在nums2中的下标
        if freq2[n]:
            fout += 1

    out[0] = fout

    fout = 0
    for n in nums2: # nums2中的值在nums1中的下标
        if freq1[n]:
            fout += 1

    out[1] = fout

    return out


if __name__ == "__main__":
    nums1 = [4, 3, 1, 1, 2]
    nums2 = [2, 2, 5, 2, 6, 3, 1]
    print(findIntersectionValues(nums1, nums2))