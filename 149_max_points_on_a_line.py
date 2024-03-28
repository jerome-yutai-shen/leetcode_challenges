# -*- coding: utf-8 -*-
"""
Created on Nov 13 14:14:59 2023

@author: Jerome Yutai Shen

"""
from typing import List
import collections
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if j != i:
                    theta = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                    cnt[theta*180/math.pi] += 1
            result = max(result, max(cnt.values()) + 1)
        print(cnt)
        return result


if __name__ == "__main__":
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    _ = Solution()
    _.maxPoints(points)