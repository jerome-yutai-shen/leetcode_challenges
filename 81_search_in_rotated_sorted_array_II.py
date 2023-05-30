# -*- coding: utf-8 -*-
"""
Created on Jun 08 05:07:54 2022

@author: Jerome Yutai Shen

"""


def search(A, target):
    # write your code here
    if not A or target is None:
        return False

    start, end = 0, len(A) - 1
    while start + 1 < end:

        while A[start] == A[start + 1] and start + 1 < end:
            start += 1
        while A[end] == A[end - 1] and start + 1 < end:
            end -= 1

        mid = start + (end - start) // 2

        if target in [A[start], A[mid], A[end]]:
            return True

        if A[mid] < A[end]:
            if A[mid] < target < A[end]:
                start = mid
            else:
                end = mid
        else:
            if A[start] < target < A[mid]:
                end = mid
            else:
                start = mid

    return target in [A[start], A[end]]