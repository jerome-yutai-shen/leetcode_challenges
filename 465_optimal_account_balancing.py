# -*- coding: utf-8 -*-
"""
Created on Jun 21 15:39:17 2023

@author: Jerome Yutai Shen

"""
from typing import List
import collections


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = collections.defaultdict(int)
        for a, b, amount in transactions:
            balance_map[a] += amount
            balance_map[b] -= amount

        balance_list = [amount for amount in balance_map.values() if amount]
        n = len(balance_list)

        memo = [-1] * (1 << n)
        memo[0] = 0

        def dfs(total_mask):
            if memo[total_mask] != -1:
                return memo[total_mask]
            balance_sum, answer = 0, 0

            # Remove one person at a time in total_mask
            for i in range(n):
                cur_bit = 1 << i
                if total_mask & cur_bit:
                    balance_sum += balance_list[i]
                    answer = max(answer, dfs(total_mask ^ cur_bit))

            # If the total balance of total_mask is 0, increment answer by 1.
            memo[total_mask] = answer + (balance_sum == 0)
            return memo[total_mask]

        return n - dfs((1 << n) - 1)


import collections

class Solution2:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        edges = transactions

        acct_with_0 = collections.defaultdict(int)
        for u, v, amt in edges:
            acct_with_0[u] += amt
            acct_with_0[v] -= amt
        debt = [v for v in acct_with_0.values() if v != 0]
        n = len(debt)
        if n == 0:
            return 0

        dp_len = 1 << n
        f = [float("inf")] * dp_len
        for comb in range(1, dp_len): # 组合从 1 开始, 不是 0.
            tot = 0
            count = 0
            for user in range(n):
                if (1 << user) & comb > 0:
                    tot += debt[user]
                    count += 1
            if tot == 0:
                f[comb] = count - 1 # 两个数额,是一笔交易, 三个数额, 两笔交易, count - 1; 比如 5, 5, -10.
                for sub_comb in range(comb): # 开区间, 不需要考虑 comb 本身, not comb + 1.
                    if sub_comb & comb == sub_comb and f[sub_comb] + f[comb - sub_comb] < f[comb]:
                        f[comb] = f[sub_comb] + f[comb - sub_comb]
        return f[-1]


import math
from collections import defaultdict
from functools import lru_cache
from itertools import combinations


class Solution3:
    def minTransfers(self, transactions):
        edges = transactions
        balances = defaultdict(int)
        for giver, receiver, amount in edges:
            balances[giver] += amount
            balances[receiver] -= amount
        balances = {k: v for k, v in balances.items() if v != 0}

        tuplify = lambda balance: tuple(sorted((k, v) for k, v in balance.items()))

        @lru_cache(maxsize=200)
        def dfs(balances_):
            if not balances_:
                return 0
            res = math.inf
            balances_ = {k: v for k, v in balances_}
            for size in range(2, len(balances_) + 1):
                for group in combinations(balances_.keys(), size):
                    if sum(balances_[p] for p in group) == 0:
                        remaining_balances = {k: v for k, v in balances_.items() if k not in group}
                        res = min(res, size - 1 + dfs(tuplify(remaining_balances)))
            return res

        return dfs(tuplify(balances))