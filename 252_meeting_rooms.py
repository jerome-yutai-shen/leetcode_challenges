# -*- coding: utf-8 -*-
"""
Created on Nov 12 16:50:19 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]: # current_end > next_start
                return False
        return True

    def canAttendMeetings2(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:  # previous_end > current_start
                return False
        return True