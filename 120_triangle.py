# -*- coding: utf-8 -*-
"""
Created on Oct 16 06:10:36 2023

@author: Jerome Yutai Shen

"""
from typing import List
import math


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])


def minimumTotal(triangle: List[List[int]]) -> int:
    for row in range(1, len(triangle)):
        for col in range(row + 1):
            smallest_above = math.inf
            if col > 0:
                smallest_above = triangle[row - 1][col - 1]
            if col < row:
                smallest_above = min(smallest_above, triangle[row - 1][col])
            triangle[row][col] += smallest_above
    return min(triangle[-1])


def minimumTotal2(triangle: List[List[int]]) -> int:
    prev_row = triangle[0]
    for row in range(1, len(triangle)):
        curr_row = []
        for col in range(row + 1):
            smallest_above = math.inf
            if col > 0:
                smallest_above = prev_row[col - 1]
            if col < row:
                smallest_above = min(smallest_above, prev_row[col])
            curr_row.append(triangle[row][col] + smallest_above)
        prev_row = curr_row
    return min(prev_row)


class Solution2:
    """
    自顶向下的多重循环实现的动态规划 无任何空间优化

    时间复杂度 O(n**2) 空间复杂度 O(n**2) 额外空间
    """

    def minimumTotal(self, triangle):
        n = len(triangle)

        # state: dp[i][j] 代表从 0, 0 走到 i, j 的最短路径值
        dp = [[0] * (i + 1) for i in range(n)]

        # initialize: 三角形的左边和右边要初始化
        # 因为他们分别没有左上角和右上角的点
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        # function: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        # i, j 这个位置是从位置 i - 1, j 或者 i - 1, j - 1 走过来的
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        # print(f"dp {dp}")
        # answer: 最后一层的任意位置都可以是路径的终点
        return min(dp[n - 1])


if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    _ = Solution2()
    _.minimumTotal(triangle)