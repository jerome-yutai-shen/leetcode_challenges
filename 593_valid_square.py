# -*- coding: utf-8 -*-
"""
Created on Jun 20 21:21:18 2023

@author: Jerome Yutai Shen

"""
from typing import (
    List,
)

class Solution:
    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p = sorted([p1, p2, p3, p4])
        bool_side_length_positive = self.dist(p[0], p[1]) > 0
        bool_four_sides_equal = self.dist(p[0], p[1]) == self.dist(p[1], p[3]) == self.dist(p[3], p[2]) == self.dist(p[2], p[0])
        bool_diagonals_equal = self.dist(p[0], p[3]) == self.dist(p[1], p[2])
        return  bool_side_length_positive and bool_four_sides_equal and bool_diagonals_equal
