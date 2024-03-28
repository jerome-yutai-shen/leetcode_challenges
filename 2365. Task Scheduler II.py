# -*- coding: utf-8 -*-
"""
Created on Nov 25 14:14:32 2023

@author: Jerome Yutai Shen

"""
from collections import defaultdict
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        runtime: O(n)
        space: O(n)
        """
        times = defaultdict(int)
        day = 0

        for task in tasks:
            day += 1
            if not times[task] or day - times[task] > space:
                times[task] = day
            else:
                diff = space - (day - times[task])
                day += diff + 1
                times[task] = day

        return day

    def taskSchedulerII2(self, tasks: List[int], space: int) -> int:
        """
        runtime: O(n)
        space: O(n)
        """
        times = defaultdict(int)
        day = 0

        for task in tasks:
            day += 1

            if task in times and day - times[task] <= space: # 一定要包括等于！
                days_pss= space - (day - times[task])
                day += days_pss + 1

            times[task] = day

        return day
