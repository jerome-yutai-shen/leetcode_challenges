# -*- coding: utf-8 -*-
"""
Created on Oct 10 18:42:36 2023

@author: Jerome Yutai Shen

"""


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        if jug1Capacity + jug2Capacity == targetCapacity or \
            jug1Capacity == targetCapacity or \
            jug2Capacity == targetCapacity:
            return True

        int_larger = max(jug1Capacity, jug2Capacity)
        int_smaller = min(jug1Capacity, jug2Capacity)
        return targetCapacity % self.gcd(int_larger, int_smaller) == 0

    def gcd(self, int_larger: int, int_smaller: int) -> int:
        return int_smaller if int_larger % int_smaller == 0 else self.gcd(int_smaller, int_larger % int_smaller)
