# -*- coding: utf-8 -*-
"""
Created on Nov 26 11:27:41 2023

@author: Jerome Yutai Shen

"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """O(1), O(1)"""
        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)