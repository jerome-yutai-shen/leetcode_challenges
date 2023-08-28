# -*- coding: utf-8 -*-
"""
Created on Jun 07 18:27:28 2022

@author: Jerome Yutai Shen

"""


def is_match(s: str, p: str) -> bool:
    if s is None or p is None:
        return False

    n, m = len(s), len(p)

    # state
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # initialization
    dp[0][0] = True
    for i in range(1, m + 1):
        dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

    # function
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')

    return dp[n][m]