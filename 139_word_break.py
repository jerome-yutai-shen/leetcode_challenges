# -*- coding: utf-8 -*-
"""
Created on May 30 18:34:47 2022

@author: Jerome Yutai Shen

"""
from typing import List


def word_break_bfs(s: str, word_dict: List[str]) -> bool:
    from collections import deque
    word_set = set(word_dict)
    idx_queue = deque([0])
    visited = set()

    while idx_queue:
        start = idx_queue.popleft()
        if start in visited:
            continue
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set:
                idx_queue.append(end)
                if end == len(s):
                    return True
        visited.add(start)
    return False


def word_break_dp(s: str, word_dict: List[str]) -> bool:
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]