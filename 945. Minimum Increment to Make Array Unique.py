# -*- coding: utf-8 -*-
"""
Created on Dec 18 20:48:55 2023

@author: Jerome Yutai Shen

"""
# Author: Huahua, Running time: 196 ms


class Solution(object):
  def minIncrementForUnique(self, A):
    A.sort()
    ans = 0
    for i in range(1, len(A)):
      if A[i] > A[i - 1]:
        continue
      ans += A[i - 1] - A[i] + 1
      A[i] = A[i - 1] + 1
    return ans