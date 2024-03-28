# -*- coding: utf-8 -*-
"""
Created on Oct 03 02:09:53 2023

@author: Jerome Yutai Shen

"""
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A

    def sortArrayByParity2(self, A):
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])