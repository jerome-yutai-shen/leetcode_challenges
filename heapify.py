# -*- coding: utf-8 -*-
"""
Created on May 31 11:16:51 2022

@author: Jerome Yutai Shen

"""


def siftup(A, k):
    print(f"k: {k} {A[k]}")
    while k != 0:
        father = (k - 1) // 2
        if A[k] > A[father]:
            break
        A[k], A[father] = A[father], A[k]
        k = father
    print(f"A: {A}")


def heapify2(A):
    for idx in range(len(A)):
        siftup(A, idx)


def heapify(A):
    for idx in reversed(range((len(A)) // 2)):
        sift_down(A, idx)


def sift_down(nums, index):
    n = len(nums)
    while index * 2 + 1 < n:
        son_index = index * 2 + 1
        if son_index + 1 < n and nums[son_index] > nums[son_index + 1]:
            son_index = son_index + 1
        if nums[son_index] >= nums[index]:
            break
        nums[index], nums[son_index] = nums[son_index], nums[index]
        index = son_index


if __name__ == "__main__":
    A = [3, 2, 1, 4, 5]
    heapify2(A)