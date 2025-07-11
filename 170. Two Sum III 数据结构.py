# -*- coding: utf-8 -*-
"""
Created on Jul 03 17:40:33 2025

@author: Jerome Yutai Shen

"""
from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        for num in self.count:
            complement = value - num
            if complement == num:
                if self.count[num] > 1:
                    return True
            elif complement in self.count:
                return True
        return False