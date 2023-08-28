# -*- coding: utf-8 -*-
"""
Created on Jun 03 21:37:45 2022

@author: Jerome Yutai Shen

"""

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for idx in range(len(haystack) - n + 1):
            if haystack[idx: idx + n] == needle:
                return idx
        return -1

if __name__ == "__main__":
    pass