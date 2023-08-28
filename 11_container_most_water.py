# -*- coding: utf-8 -*-
"""
Created on May 23 08:08:07 2022

@author: Jerome Yutai Shen

"""


from typing import List


def get_max_area(heights: List[int]) -> int:
    max_area = 0
    p_left = 0
    p_right = len(heights) - 1

    while p_left < p_right:
        width = p_right - p_left
        area = width * min(heights[p_left], heights[p_right])
        max_area = max(max_area, area)
        if heights[p_left] > heights[p_right]:
            p_right -= 1
        elif heights[p_left] < heights[p_right]:
            p_left += 1
        else:
            # heights[p_left] == heights[p_right]
            p_left += 1 # p_right -= 1 也可以。这个特殊情况可以归入上面任何一种

    return max_area