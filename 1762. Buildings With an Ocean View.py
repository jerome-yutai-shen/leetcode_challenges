# -*- coding: utf-8 -*-
"""
Created on Nov 25 15:59:55 2023

@author: Jerome Yutai Shen

"""
from typing import List


class Solution:
    def findBuildings2(self, heights: List[int]) -> List[int]:
        """O(N), O(N)"""
        n = len(heights)
        answer = []

        for current in range(n):
            # If the current building is taller,
            # it will block the shorter building's ocean view to its left.
            # So we pop all the shorter buildings that have been added before.
            while answer and heights[answer[-1]] <= heights[current]:
                answer.pop()
            answer.append(current)

        return answer

    def findBuildings(self, heights: List[int]) -> List[int]:
        """O(N), O(1)"""
        n = len(heights)
        answer = []
        max_height = -1

        for current in range(n)[::-1]: # 反过来从尾到头比较
            # If there is no building higher (or equal) than the current one to its right,
            # push it in the answer array.

            if max_height < heights[current]:
                answer.append(current)

                # Update max building till now.
                max_height = heights[current]

        return answer[::-1] #最终结果再反回来一次