# -*- coding: utf-8 -*-
"""
Created on Nov 26 19:51:06 2023

@author: Jerome Yutai Shen

"""

def canPermutePalindrome(s: str) -> bool:
    new_set = set()
    for char in s:
        if char not in new_set:
            new_set.add(char)
        else:
            new_set.remove(char)
    return len(new_set) <= 1