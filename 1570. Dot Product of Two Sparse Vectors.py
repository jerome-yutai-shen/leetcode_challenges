# -*- coding: utf-8 -*-
"""
Created on Nov 25 16:30:21 2023

@author: Jerome Yutai Shen

"""
from typing import List


class SparseVector:
    """
    O(n) for creating the <index, value> pair for non-zero values
    O(L+L2) for calculating the dot product.
    O(L) for creating the <index, value> pairs for non-zero values.
    O(1) for calculating the dot product.
    """
    def __init__(self, nums: List[int]):
        self.pairs = { }
        self.indices = set()
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs[index] = value
                self.indices.add(index)

    def dotProduct2(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        intersect = self.indices.intersection(vec.indices)
        if not intersect:
            return result

        for index in intersect:
            result += self.pairs[index] * vec.pairs[index]

        return result


class SparseVector2:
    def __init__(self, nums: List[int]):
        """
        Let n be the length of the input array
        and L be the number of non-zero elements.
        O(N), O(L)
        """
        self.nonzeros = { }
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result


class SparseVector3:
    """O(N), O(1)"""
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result