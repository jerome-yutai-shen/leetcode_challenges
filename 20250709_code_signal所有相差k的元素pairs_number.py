# -*- coding: utf-8 -*-
"""
Created on Jul 09 09:11:27 2025

@author: Jerome Yutai Shen

"""
from collections import Counter

def solution(k, a):
    MOD = 10**9 + 7
    freq = Counter(a)
    count = 0

    for x in freq:
        if x + k in freq:
            count += freq[x] * freq[x + k]

    return count % MOD