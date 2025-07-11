# -*- coding: utf-8 -*-
"""
Created on Jul 05 21:51:12 2025

@author: Jerome Yutai Shen

"""
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s_count = Counter()
        g_count = Counter()

        for s_char, g_char in zip(secret, guess):
            if s_char == g_char:
                bulls += 1
            else:
                s_count[s_char] += 1
                g_count[g_char] += 1

        # cows = min(secret中有的, guess中错位也有的)
        for char in g_count:
            cows += min(s_count[char], g_count[char])

        return f"{bulls}A{cows}B"
