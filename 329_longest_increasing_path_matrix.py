# -*- coding: utf-8 -*-
"""
Created on Jun 21 01:26:56 2023

@author: Jerome Yutai Shen

"""
DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        sequence = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sequence.append((matrix[i][j], i, j))
        sequence.sort()

        check = { }
        for h, x, y in sequence:
            cur_pos = (x, y)
            if cur_pos not in check:
                check[cur_pos] = 1
            cur_path = 0
            for dx, dy in DIRECTIONS:
                if self.is_valid(x + dx, y + dy, matrix, h):
                    cur_path = max(cur_path, check[(x + dx, y + dy)])
            check[cur_pos] += cur_path

        vals = check.values()
        return max(vals)

    def is_valid(self, x, y, matrix, h):
        row, col = len(matrix), len(matrix[0])
        return x >= 0 and x < row and y >= 0 and y < col and matrix[x][y] < h



if __name__ == "__main__":
    matrix = [[9, 8, 3], [9, 2, 1], [6, 5, 7]]
    sequence = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sequence.append((matrix[i][j], i, j))
    sequence.sort()
