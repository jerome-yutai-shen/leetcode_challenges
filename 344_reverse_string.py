# -*- coding: utf-8 -*-
"""
Created on May 30 14:59:08 2022

@author: Jerome Yutai Shen

"""


def reverse_string(src_str: str):
    """
    two pointers
    """
    left, right = 0, len(src_str) - 1
    while left < right:
        src_str[left], src_str[right] = src_str[right], src_str[left]
        left, right = left + 1, right - 1


def reverse_string2(s: str):
    p_left, p_right = 0, len(s) - 1
    while p_left <= p_right:
        s[p_right], s[p_left] = s[p_left], s[p_right]
        p_left += 1
        p_right -= 1

    return s