# -*- coding: utf-8 -*-
"""
Created on Jun 07 13:48:58 2022

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def trap_rain_water(self, heights: List[int]) -> int:
        """
        stack approach
        :param heights:
        :return:
        """
        if not heights:
            return len(heights)

        sum = 0
        stack = []
        current = 0
        while current < len(heights):
            while len(stack) and heights[current] > heights[stack[-1]]:
                h = heights[stack.pop()]
                if not len(stack): break
                distance = current - stack[-1] - 1
                _min = min(heights[stack[-1]], heights[current])
                sum += distance * (_min - h)
            stack.append(current)
            current += 1
        return sum

    def trap_rain_water_dp(self, heights: List[int]) -> int:
        if not heights:
            return len(heights)
        sum = 0
        max_left = [0 for _ in heights]
        max_right = [0 for _ in heights]
        for idx in range(1, len(heights) - 1):
            max_left[idx] = max(max_left[idx - 1], heights[idx - 1])
        for idx in range(len(heights) - 2, -1, -1):
            max_right[idx] = max(max_right[idx + 1], heights[idx + 1])
        for idx in range(1, len(heights) - 1):
            _min = min(max_left[idx], max_right[idx])
            if (_min > heights[idx]): sum += _min - heights[idx]
        return sum