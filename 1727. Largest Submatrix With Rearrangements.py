# -*- coding: utf-8 -*-
"""
Created on Nov 27 09:00:33 2023

@author: Jerome Yutai Shen

"""


class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m = len(matrix)
        n = len(matrix[0])
        height = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    height[j] += 1
                else:
                    height[j] = 0

            for j, h in enumerate(sorted(height, reverse=True)):
                res = max(res, (j + 1) * h)

        return res
