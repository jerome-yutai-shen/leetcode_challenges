# -*- coding: utf-8 -*-
"""
Created on Jun 08 03:30:49 2022

@author: Jerome Yutai Shen

"""


def climbStairs_dp(n: int) -> int:
    if n < 3:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for idx in range(3, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    return dp[n]


def climbStairs_dp_refined(n: int) -> int:
    if n < 3:
        return n
    prev, curr = 1, 2
    for i in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr

if __name__ == "__main__":
    print(climbStairs_dp_refined(3))