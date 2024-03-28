# -*- coding: utf-8 -*-
"""
Created on Oct 03 02:23:57 2023

@author: Jerome Yutai Shen

"""
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing