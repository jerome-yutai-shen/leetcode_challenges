# -*- coding: utf-8 -*-
"""
Created on Sep 17 23:53:35 2023

@author: Jerome Yutai Shen

"""
from functools import lru_cache
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """
    O(S * n), O(n)
    """
    @lru_cache(None)
    def dfs(rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        min_cost = float('inf')
        for coin in coins:
            res = dfs(rem - coin)
            if res != -1:
                min_cost = min(min_cost, res + 1)
        return min_cost if min_cost != float('inf') else -1

    return dfs(amount)

def coinChange2(coins: List[int], amount: int) -> int:
    """
    O(S * n), O(n)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1