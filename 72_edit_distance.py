# -*- coding: utf-8 -*-
"""
Created on Jun 08 04:18:17 2022

@author: Jerome Yutai Shen

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i  # 将长度为i的字符串word1[:i+1]转化为空字符串所需的编辑距离
        for j in range(n + 1):
            dp[0][j] = j  # 将空字符串转化为长度为j的字符串word2[:j+1]所需的编辑距离

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, temp)

        return dp[m][n]